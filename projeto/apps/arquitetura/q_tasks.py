import time

from post_office import mail


def tarefa(n):
    time.sleep(n)
    return f'Tempo de espera da tarefa: {n}'


def enviar_email(task):
    mail.send(
        ['recipient@domain.com'],
        'sender@domain.com',
        subject='Assunto do email',
        message=task.result,
        priority='now',
    )
