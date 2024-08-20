#!/usr/bin/env python3
import os

os.system('service nginx start')
comandos = [
    'poetry lock --no-update',
    'poetry install --no-root',
    'poetry run inv collectstatic --settings=production --clear',
    'poetry run inv migrate --settings=production',
    'poetry run inv celery --settings=production &',
    'poetry run inv gunicorn',
]
os.system('\n'.join(comandos))
