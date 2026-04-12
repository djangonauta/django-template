from django.contrib import auth
from factory import django
from factory.faker import Faker
from factory.helpers import lazy_attribute

from .models import Produto


class UsuarioFactory(django.DjangoModelFactory):
    username = Faker("first_name")
    password = Faker("ean")

    class Meta:
        model = auth.get_user_model()
        django_get_or_create = ("username", "email")

    @lazy_attribute
    def email(self):
        return f"{self.username}@domain.com"


class ProdutoFactory(django.DjangoModelFactory):
    descricao = Faker("sentence", nb_words=5)
    preco = Faker("pydecimal", left_digits=3, right_digits=2, positive=True, min_value=1)

    class Meta:
        model = Produto
