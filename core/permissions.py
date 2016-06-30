"""Permissões customizadas da aplicação core."""

from rest_framework.permissions import BasePermission


class IsAdminOnly(BasePermission):
    """Permissão de acesso apenas ao admin."""

    def has_permission(self, request, view):
        """Verifica se essa solicitação é permitida."""
        return request.user.is_superuser
