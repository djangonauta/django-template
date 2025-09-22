from django.contrib.auth.models import UserManager
from django.db.models import IntegerChoices


class TipoUsuario(IntegerChoices):
    DEFAULT = 1, "default"


class UsuarioManager(UserManager):
    pass
