from django.contrib import auth
from factory import django
from factory.faker import Faker
from factory.helpers import lazy_attribute


class UsuarioFactory(django.DjangoModelFactory):
    username = Faker("first_name")
    password = Faker("ean")

    class Meta:
        model = auth.get_user_model()
        django_get_or_create = ("username", "email")

    @lazy_attribute
    def email(self):
        return "{}@domain.com".format(self.username)
