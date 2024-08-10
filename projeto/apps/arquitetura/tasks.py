import time

from django.conf import settings
from django.core import mail

from projeto.celery import app


@app.task
def email_admins_teste(mensagem):
    time.sleep(6)
    mail.send_mail('tarefa teste', f'Tarefa teste enviada via celery worker\n{mensagem}',
                   from_email=settings.DEFAULT_FROM_EMAIL,
                   recipient_list=dict(settings.ADMINS).values())
    return mensagem
