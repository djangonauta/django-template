"""Configuração para deploy no heroku."""

from .production import *

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# amazon s3
AWS_STORAGE_BUCKET_NAME = '{{ project_name }}-staging'
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
STATICFILES_LOCATION = 'static'
# STATICFILES_STORAGE = 'core.storages.StaticLocationStorage'
MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'core.storages.MediaLocationStorage'
