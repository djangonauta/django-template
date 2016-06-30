"""Configuração de administração da aplicação core."""

from django.contrib.admin import ModelAdmin, register
from django.contrib.auth import get_user_model


@register(get_user_model())
class UserAdmin(ModelAdmin):
    """Registra o usuário base na aplicação admin."""

    pass
