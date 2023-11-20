import random

import factory

from . import models

CATEGORIAS = ('eletrônico', 'eletrodoméstico', 'papelaria', 'celulares')
PRODUTOS = ('teclado', 'monitor', 'processador', 'liquidificador', 'sapato', 'papel A4')


class CategoriaFactory(factory.django.DjangoModelFactory):

    nome = factory.Iterator(CATEGORIAS)

    class Meta:

        model = models.Categoria
        django_get_or_create = ('nome',)


class FornecedorFactory(factory.django.DjangoModelFactory):

    nome = factory.Faker('company', locale='pt_BR')

    class Meta:

        model = models.Fornecedor
        django_get_or_create = ('nome',)


class ClienteFactory(factory.django.DjangoModelFactory):

    nome = factory.Faker('first_name', locale='pt_BR')

    class Meta:

        model = models.Cliente
        django_get_or_create = ('nome',)


class ProdutoFactory(factory.django.DjangoModelFactory):

    fornecedor = factory.SubFactory(FornecedorFactory)

    @factory.post_generation
    def categorias(self, created, extracted, **kwargs):
        if not created or not extracted:
            return

        extracted = random.choices(extracted, k=random.randint(1, len(extracted)))
        self.categorias.add(*extracted)

    nome = factory.Iterator(PRODUTOS)

    @factory.LazyAttribute
    def preco(self):
        return random.randint(1, 5000)

    class Meta:

        model = models.Produto
        django_get_or_create = ('nome', 'preco')
