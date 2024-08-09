from django.apps import AppConfig


class UsuariosConfig(AppConfig):

    name = 'projeto.apps.administrativo.usuarios'

    def ready(self):
        from . import signals  # noqa: F401
