"""Modelos da aplicação core."""

from django.contrib.auth import models
from model_utils import models as model_utils_models


class User(model_utils_models.TimeStampedModel, models.AbstractUser):
    """Usuário base do projeto."""

    class Meta:
        verbose_name = 'Usuário'
