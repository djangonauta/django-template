from django.contrib import auth
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UsuarioSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        # return dict(id=instance.id, text=instance.nome_completo) # select2
        return super().to_representation(instance)

    class Meta:
        model = auth.get_user_model()
        fields = ['id', 'username', 'nome_completo']


class DisableSignupSerializer(serializers.Serializer):

    def validate(self, data):
        raise serializers.ValidationError('Registro de novas contas temporariamente suspenso.')


class TokenParComPermissoesSerializer(TokenObtainPairSerializer):
    def get_token(self, user):
        token = super().get_token(user)
        token['permissions'] = list(user.get_all_permissions())
        token['is_admin'] = user.is_superuser
        return token
