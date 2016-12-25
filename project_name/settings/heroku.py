"""Configuração para deploy no heroku."""

from .production import *

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# amazon s3
AWS_STORAGE_BUCKET_NAME = 'slidecoins-staging'
AWS_ACCESS_KEY_ID = get_environment_variable('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = get_environment_variable('AWS_SECRET_ACCESS_KEY')
STATICFILES_LOCATION = 'static'
# STATICFILES_STORAGE = 'core.storages.StaticLocationStorage'
MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'core.storages.MediaLocationStorage'
