"""Fábricas da aplicação core."""

from django.contrib.auth import get_user_model
from factory import Faker, lazy_attribute
from factory.django import DjangoModelFactory


class UserFactory(DjangoModelFactory):
    """Fábrica de usuários."""

    username = Faker('first_name')
    password = Faker('ean')

    @lazy_attribute
    def email(self):
        """Email aleatório."""
        return '{}@domain.com'.format(self.username)

    class Meta:
        model = get_user_model()
        django_get_or_create = ('username', 'email')
