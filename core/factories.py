"""Fábricas da aplicação core."""

import factory
from django.contrib import auth
from factory import django


class UserFactory(django.DjangoModelFactory):
    """Fábrica de usuários."""

    username = factory.Faker('first_name')
    password = factory.Faker('ean')

    @factory.lazy_attribute
    def email(self):
        """Email aleatório."""
        return '{}@domain.com'.format(self.username)

    class Meta:
        model = auth.get_user_model()
        django_get_or_create = ('username', 'email')
