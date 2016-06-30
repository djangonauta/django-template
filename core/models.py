"""Modelos da aplicação core."""

from django.contrib.auth.models import AbstractUser

from model_utils.models import TimeStampedModel


class User(TimeStampedModel, AbstractUser):
    """Usuário base do projeto."""

    class Meta:
        verbose_name = 'Usuário'
