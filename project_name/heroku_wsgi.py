"""Configuração Heroku wsgi do projeto slidecoins."""

import os

from django.core import wsgi
from whitenoise import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings.heroku")
application = django.DjangoWhiteNoise(wsgi.get_wsgi_application())
