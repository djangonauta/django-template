#!/usr/bin/env python3
import os

comandos = [
    "poetry install --without dev --sync --compile",
    "poetry run inv collectstatic --clear",
    "poetry run inv migrate --merge",
    "poetry run inv gunicorn",
]
os.system("\n".join(comandos))
