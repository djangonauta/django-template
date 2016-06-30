"""Testes relacionados ao comandos customizados da aplicação core."""

from tempfile import NamedTemporaryFile
from unittest import TestCase

from ..management.commands.add_static_tags import Command


class CommandsTests(TestCase):
    """Testa comandos da aplicação."""

    @classmethod
    def setUpClass(cls):
        """
        Inicializa os arquivos teste.

        Esses arquivos são criados em /tmp e são excluídos na reinicialização do sistema.
        """
        super().setUpClass()

        cls.href_file = NamedTemporaryFile('w+t', delete=False)
        cls.src_file = NamedTemporaryFile('w+t', delete=False)
        cls.multi_file = NamedTemporaryFile('w+t', delete=False)
        cls.multi_tag = NamedTemporaryFile('w+t', delete=False)

        with cls.href_file as f:
            f.write('<link rel="stylesheet" href="/static/css/style.css" />')

        with cls.src_file as f:
            f.write('<script src="/static/js/script.js"></script>')

        with cls.multi_file as f:
            f.write('<link rel="stylesheet" href="/static/css/style.css" />\n')
            f.write('<script src="/static/js/script.js"></script>')

        with cls.multi_tag as f:
            f.write('<link rel="stylesheet" href="/static/css/style.css" />'
                    '<script src="/static/js/script.js"></script>')

    def test_add_static_tags_href(self):
        """Testa o comando add_static_tags utilizando href."""
        Command().replace(self.href_file.name)
        with open(self.href_file.name) as f:
            self.assertEqual(
                f.read(),
                """<link rel="stylesheet" href="{% templatetag openblock %} static 'css/style.css' """
                """{% templatetag closeblock %}" />""",
            )

    def test_add_static_tags_src(self):
        """Testa o comando add_static_tags utilizando src."""
        Command().replace(self.src_file.name)
        with open(self.src_file.name) as f:
            self.assertEqual(
                f.read(),
                """<script src="{% templatetag openblock %} static 'js/script.js' """
                """{% templatetag closeblock %}"></script>""",
            )

    def test_add_static_tags_multiple_lines(self):
        """Testa o comando add_static_tags em multiplas linhas."""
        Command().replace(self.multi_file.name)
        with open(self.multi_file.name) as f:
            self.assertEqual(
                f.read(),
                """<link rel="stylesheet" href="{% templatetag openblock %} static 'css/style.css' """
                """{% templatetag closeblock %}" />"""
                """\n<script src="{% templatetag openblock %} static 'js/script.js' """
                """{% templatetag closeblock %}"></script>""",
            )

    def test_add_static_tags_multiple_tags(self):
        """Testa o comando add_static_tags em multiplas tags em uma linha."""
        Command().replace(self.multi_tag.name)
        with open(self.multi_tag.name) as f:
            self.assertEqual(
                f.read(),
                """<link rel="stylesheet" href="{% templatetag openblock %} static 'css/style.css' """
                """{% templatetag closeblock %}" />"""
                """<script src="{% templatetag openblock %} static 'js/script.js' """
                """{% templatetag closeblock %}"></script>""",
            )
