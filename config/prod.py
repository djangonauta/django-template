#!/usr/bin/env python3
import os

os.system('service nginx start')
comandos = [
    'poetry lock --no-update',
    'poetry install --no-root',
    'poetry run inv collectstatic --settings=production',
    'poetry run inv migrate --settings=production',
    'poetry run inv celery --settings=production &',
    ('poetry run gunicorn --pid /run/gunicorn/pid --access-logfile /var/log/gunicorn/acesso.log --log-file '
     '/var/log/gunicorn/app.log --capture-output --enable-stdio-inheritance --workers 4 --bind 0.0.0.0:8000 '
     'projeto.wsgi')
]
os.system('\n'.join(comandos))
