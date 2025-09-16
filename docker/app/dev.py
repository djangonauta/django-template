#!/usr/bin/env python3
import os

comandos = [
    "poetry install --with dev",
    "poetry run inv migrate --settings=development --merge",
    "poetry run inv tests",
    "poetry run inv runserver",
]
os.system("\n".join(comandos))
