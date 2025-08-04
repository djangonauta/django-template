# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/
from .base import *  # noqa: F403

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG  # noqa: F405

# Django Debug Toolbar
INSTALLED_APPS += ['debug_toolbar']  # noqa: F405
INTERNAL_IPS = ['127.0.0.1']

MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')  # noqa: F405

MEDIA_ROOT = BASE_DIR / 'uploads-dev'  # noqa: F405

LOGGING['loggers']['projeto.apps']['level'] = 'DEBUG'  # noqa: F405
LOGGING['loggers']['celery']['level'] = 'DEBUG'  # noqa: F405
LOGGING['handlers']['json_file']['filename'] = 'logs/projeto.json.log'  # noqa: F405
LOGGING['handlers']['flat_line_file']['filename'] = 'logs/projeto.flat_line.log'  # noqa: F405
LOGGING['handlers']['celery_json_file']['filename'] = 'logs/celery.json.log'  # noqa: F405
LOGGING['handlers']['celery_flat_line_file']['filename'] = 'logs/celery.flat_line.log'  # noqa: F405

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'].append(  # noqa: F405
    'rest_framework.renderers.BrowsableAPIRenderer'
)
