"""Comandos customizados da aplicação core."""

import re
from fileinput import FileInput

from django.core.management.base import BaseCommand
from django.template.loader import get_template

pattern = re.compile(r'(src|href)=".+?static/(.+?)"')


class Command(BaseCommand):
    """Insere static tags em atributos 'src' e 'href' mantendo a url/uri original."""

    def add_arguments(self, parser):
        """Adiciona opções da linha de comando."""
        parser.add_argument('files', nargs='+')

    def replace(self, path):
        """
        Insere static tags em scripts e styles.

        Esse passo é necessário já que bower é utilizado para injetar arquivos js/css e ele remove static
        tags previamente inseridas.
        """
        with FileInput(path, inplace=True) as f:
            for line in f:
                repl = r'''\1="{% templatetag openblock %} static '\2' {% templatetag closeblock %}"'''
                line = pattern.sub(repl, line)
                print(line, end='')

    def handle(self, *args, **options):
        """Executa o comando."""
        paths = [get_template(t).template.origin.name for t in options['files']]
        for path in paths:
            self.replace(path)
