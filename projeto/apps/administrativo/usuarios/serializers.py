from django.contrib import auth
from rest_framework import serializers


class UsuarioSerializer(serializers.ModelSerializer):

    nome_completo = serializers.ReadOnlyField(source='get_full_name')

    def to_representation(self, instance):
        usuario_dict = super().to_representation(instance)
        nome = usuario_dict.get('nome_completo', '') or usuario_dict['username']
        return dict(id=usuario_dict['id'], text=nome)

    class Meta:
        model = auth.get_user_model()
        fields = ['id', 'username', 'nome_completo']


class DisableSignupSerializer(serializers.Serializer):

    def validate(self, data):
        raise serializers.ValidationError('Registro de novas contas temporariamente suspenso.')
