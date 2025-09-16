import logging.config
import os

from celery import Celery
from celery.signals import setup_logging
from django.conf import settings
from django_structlog.celery.steps import DjangoStructLogInitStep

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projeto.settings")

app = Celery("projeto")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
if app.steps is not None:
    app.steps["worker"].add(DjangoStructLogInitStep)


@setup_logging.connect
def receiver_setup_logging(loglevel, logfile, format, colorize, **kwargs):  # pragma: no cover
    logging.config.dictConfig(settings.LOGGING)
