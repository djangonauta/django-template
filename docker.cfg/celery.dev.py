#!/usr/bin/env python3
import os

comandos = [
    'poetry install --with dev --sync',
    'poetry run inv celery --settings development',
]
os.system('\n'.join(comandos))
