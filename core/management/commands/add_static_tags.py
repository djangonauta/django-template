"""Comandos customizados da aplicação core."""

import fileinput
import logging
import re

from django.core.management import base
from django.template import loader

logger = logging.getLogger(__name__)


class Command(base.BaseCommand):
    """Insere static tags em atributos 'src' e 'href' mantendo a url/uri original."""

    pattern = re.compile(r'(src|href)=".+?static/(.+?)"')

    def add_arguments(self, parser):
        """Adiciona opções da linha de comando."""
        parser.add_argument('files', nargs='+')

    def replace(self, path):
        """
        Insere static tags em scripts e styles.

        Esse passo é necessário já que bower é utilizado para injetar arquivos js/css e ele remove static
        tags previamente inseridas.
        """
        with fileinput.FileInput(path, inplace=True) as f:
            for line in f:
                repl = r'''\1="{% templatetag openblock %} static '\2' {% templatetag closeblock %}"'''
                line = self.pattern.sub(repl, line)
                print(line, end='')

    def handle(self, *args, **options):
        """Executa o comando."""
        logger.debug('Obtendo templates para substituição...')

        paths = [loader.get_template(t).template.origin.name for t in options['files']]
        logger.debug('Templates encontrados: %s', paths)

        for path in paths:
            logger.debug('Substituindo template %s', path)
            self.replace(path)
            logger.debug('Template substituido com sucesso.')
