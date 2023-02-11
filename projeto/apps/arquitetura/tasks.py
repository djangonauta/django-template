import time

from projeto.celery import app


@app.task
def somar(*elementos):
    time.sleep(5)
    return sum(elementos)
