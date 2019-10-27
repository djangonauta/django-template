"""Api da aplicação usuarios."""

from django.contrib import auth
from rest_framework import permissions, viewsets

from . import serializers


class UsuarioViewSet(viewsets.ModelViewSet):
    """User viewset."""

    serializer_class = serializers.UsuarioSerializer
    permission_classes = (permissions.IsAdminUser,)
    queryset = auth.get_user_model().objects.all()
