#!/usr/bin/env python3
import os

comandos = [
    'poetry lock --no-update',
    'poetry install --with dev --sync',
    'poetry run inv migrate --settings=development --merge',
    'poetry run inv tests',
    'poetry run inv celery --settings=development &',
    'poetry run inv runserver',
]
os.system('\n'.join(comandos))
