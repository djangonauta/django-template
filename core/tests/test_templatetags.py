"""Testes relacionados a tags e filtros da aplicação core."""

import hashlib
import unittest

from ..templatetags import core_tags


class CoreSimpleTagsTests(unittest.TestCase):
    """Testes de tags simples."""

    def test_gravatar_url(self):
        """Verifica se a url gravatar é gerada corretamente em função do email fornecido."""
        email = 'admin@domain.com'
        hash_email = hashlib.md5(email.encode('utf-8')).hexdigest()

        url = core_tags.gravatar_url(email)
        self.assertEqual(url, '//www.gravatar.com/avatar/{}'.format(hash_email))
