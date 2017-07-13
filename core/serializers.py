"""Serializadores da aplicação core."""

from django.contrib import auth
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """User serializer."""

    gravatar_url = serializers.ReadOnlyField(source='get_gravatar_url')
    full_name = serializers.ReadOnlyField(source='get_full_name')

    class Meta:
        model = auth.get_user_model()
        fields = ['id', 'username', 'gravatar_url', 'full_name', 'created']


class DisableSignupSerializer(serializers.Serializer):
    """Serializador customizado para processo de registro."""

    def validate(self, data):
        """Desativa a criação de novas contas."""
        raise serializers.ValidationError('Registro de novas contas temporariamente suspenso.')
