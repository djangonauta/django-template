"""Modelos da aplicação core."""

from django.contrib.auth import models


class User(models.AbstractUser):
    """Usuário base do projeto."""

    class Meta:
        """Model meta."""

        verbose_name = 'Usuário'
