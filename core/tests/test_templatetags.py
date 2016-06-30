"""Testes relacionados a tags e filtros da aplicação core."""

from hashlib import md5
from unittest import TestCase

from ..templatetags.core_tags import gravatar_url


class CoreSimpleTagsTests(TestCase):
    """Testes de tags simples."""

    def test_gravatar_url(self):
        """Verifica se a url gravatar é gerada corretamente em função do email fornecido."""
        email = 'admin@domain.com'
        hash_email = md5(email.encode('utf-8')).hexdigest()

        url = gravatar_url(email)
        self.assertEqual(url, '//www.gravatar.com/avatar/{}'.format(hash_email))
