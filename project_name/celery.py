"""Módulo de configuração celery."""

import os

import celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{{ project_name }}.settings')

app = celery.Celery('{{ project_name }}')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
