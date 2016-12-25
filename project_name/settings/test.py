"""Configurações de teste."""

from .development import *

PASSWORD_HASHERS = ['django.contrib.auth.hashers.MD5PasswordHasher']
MEDIA_ROOT = 'test_media'
