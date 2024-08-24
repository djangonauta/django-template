#!/usr/bin/env python3
import os

os.system('service nginx start')
comandos = [
    'poetry lock --no-update',
    'poetry install --without dev --sync --compile',
    'poetry run inv collectstatic --clear',
    'poetry run inv migrate --merge',
    'poetry run inv celery &',
    'poetry run inv gunicorn',
]
os.system('\n'.join(comandos))
