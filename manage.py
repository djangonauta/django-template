#!/usr/bin/env python3.5
"""Módulo de administração django."""

from os import environ
from sys import argv

from django.core.management import execute_from_command_line

environ.setdefault('DJANGO_SETTINGS_MODULE', '{{ project_name }}.settings')
execute_from_command_line(argv)
