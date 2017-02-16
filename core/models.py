"""Modelos da aplicação core."""

import hashlib

from django.contrib.auth import models
from model_utils.models import TimeStampedModel


class User(TimeStampedModel, models.AbstractUser):
    """Usuário base do projeto."""

    def get_gravatar_url(self):
        """Obtém a URL gravatar para esse usuário."""
        return '//www.gravatar.com/avatar/{}'.format(hashlib.md5(self.email.encode('utf-8')).hexdigest())

    class Meta:
        verbose_name = 'Usuário'
