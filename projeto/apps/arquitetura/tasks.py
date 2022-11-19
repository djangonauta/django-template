import time

from projeto.celery import app


@app.task
def tarefa(a, b):
    time.sleep(5)
    return a + b
