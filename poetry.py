#!/usr/bin/env python3
import os

comandos = [
    'poetry lock --no-update',
    'poetry install --with dev --no-root',
    'poetry run ./manage.py makemigrations',
    'poetry run ./manage.py migrate',
    'poetry run inv celery &'
    'poetry run inv'
]
os.system('\n'.join(comandos))
