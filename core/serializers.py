"""Serializadores da aplicação core."""

from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer, Serializer, ValidationError


class UserSerializer(ModelSerializer):
    """User serializer."""

    class Meta:
        model = get_user_model()
        fields = ['id', 'username']


class DisableSignupSerializer(Serializer):
    """Serializador customizado."""

    def validate(self, data):
        """Desativa a criação de novas contas."""
        raise ValidationError('Registro de novas contas temporariamente suspenso.')
