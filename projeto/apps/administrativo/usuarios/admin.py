from django.contrib import admin, auth
from django.contrib.auth.admin import UserAdmin


@admin.register(auth.get_user_model())
class UsuarioModelAdmin(UserAdmin):
    pass
