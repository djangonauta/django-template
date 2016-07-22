"""Testa mixins da aplicação core."""

import unittest

from rest_framework import serializers

from .. import mixins


class MySerializer(serializers.Serializer):
    """Serializador para testes."""

    nome = serializers.CharField()
    idade = serializers.IntegerField()
    profissão = serializers.CharField()


class MySerializerWithSelectedFields(mixins.SelectSerializerFieldsMixin, MySerializer):
    """Adiciona o mixin para redefinir campos."""


class TestSelectSerializerFieldsMixin(unittest.TestCase):
    """Testa o mixin que seleciona quais campos devem ser utilizados por um dado serializador."""

    def test_new_fields(self):
        """Verifica se os campos são definidos adequadamente."""
        data = dict(nome='dev', idade=32, profissão='developer')
        original_serializer = MySerializer(data=data)
        self.assertTrue(original_serializer.is_valid())
        self.assertDictEqual(original_serializer.data, data)

        new_serializer = MySerializerWithSelectedFields(
            data=dict(nome='developer', idade=40, profissão='Django Developer'),
            selected_field_names=['nome', 'idade']
        )
        self.assertTrue(new_serializer.is_valid())
        self.assertDictEqual(new_serializer.data, dict(nome='developer', idade=40))
