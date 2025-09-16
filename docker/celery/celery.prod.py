#!/usr/bin/env python3
import os

comandos = [
    "poetry install --without dev --sync --compile",
    "poetry run inv celery",
]
os.system("\n".join(comandos))
