from django.contrib import auth
from rest_framework import serializers

from . import models


class UsuarioSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        # return dict(id=instance.id, text=instance.nome_completo) # select2
        return super().to_representation(instance)

    class Meta:
        model = auth.get_user_model()
        fields = ['id', 'username', 'nome_completo']


class UnidadeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Unidade
        fields = ['id', 'nome', 'codigo', 'hierarquia']


class VinculoSerializer(serializers.ModelSerializer):

    unidade = UnidadeSerializer()
    responsabilidade = serializers.CharField(source='get_responsabilidade_display')

    class Meta:
        model = models.Vinculo
        fields = ['id', 'unidade', 'responsabilidade', 'ativo']


class DisableSignupSerializer(serializers.Serializer):

    def validate(self, data):
        raise serializers.ValidationError('Registro de novas contas temporariamente suspenso.')
