"""Módulo de configuração celery."""

from os import environ

from django.conf import settings

from celery import Celery

app = Celery('{{ project_name }}')
app.config_from_object(environ['DJANGO_SETTINGS_MODULE'])
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
