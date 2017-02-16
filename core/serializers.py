"""Serializadores da aplicação core."""

from django.contrib import auth
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """User serializer."""

    gravatar_url = serializers.ReadOnlyField(source='get_gravatar_url')

    class Meta:
        model = auth.get_user_model()
        fields = ['id', 'username', 'gravatar_url', 'created']


class DisableSignupSerializer(serializers.Serializer):
    """Serializador customizado."""

    def validate(self, data):
        """Desativa a criação de novas contas."""
        raise serializers.ValidationError('Registro de novas contas temporariamente suspenso.')
