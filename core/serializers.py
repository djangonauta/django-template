"""Serializadores da aplicação core."""

from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    """User serializer."""

    class Meta:
        model = get_user_model()
        fields = ['id', 'username']
