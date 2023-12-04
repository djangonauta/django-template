from django.contrib import admin, auth
from django.contrib.auth.admin import UserAdmin

from . import models


@admin.register(auth.get_user_model())
class UsuarioModelAdmin(UserAdmin):
    pass


@admin.register(models.Unidade)
class UnidadeAdmin(admin.ModelAdmin):
    pass
