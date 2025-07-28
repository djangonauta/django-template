import pathlib

import environ
import structlog
from django.conf import global_settings

env = environ.Env()
environ.Env.read_env()

# ADMINS = 'Fulano=fulano@email.com,Beltrano=beltrano@email.com'
admins = env.dict('ADMINS')
ADMINS = admins.items()
MANAGERS = env.dict('MANAGERS', default=admins).items()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = pathlib.Path(__file__).resolve().parent.parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {'default': env.db()}
DATABASES['default']['ATOMIC_REQUESTS'] = True

# Email
# https://docs.djangoproject.com/en/dev/topics/email/
env.EMAIL_SCHEMES.update(postoffice='post_office.EmailBackend')
vars().update(env.email_url())

# default charset in django.core.email.
DEFAULT_CHARSET = env('DEFAULT_CHARSET', default='utf-8')
# default from_email in EmailMessage.
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL', default='webmaster@localhost')
# default prefix + subject in mail_admins/managers.
EMAIL_SUBJECT_PREFIX = env('EMAIL_SUBJECT_PREFIX', default='[Django]')
# default from: header in mail_admins/managers.
SERVER_EMAIL = env('SERVER_EMAIL', default='admin@localhost')

# Application definition
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.messages',
    'django.contrib.postgres',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
]

PROJECT_APPS = [
    'projeto.apps.administrativo',
    'projeto.apps.administrativo.usuarios',
    'projeto.apps.arquitetura',
]

THIRD_PARTY_APPS = [
    'auditlog',
    'corsheaders',
    'django_celery_beat',
    'django_celery_results',
    'django_extensions',
    'django_filters',
    'django_structlog',
    'drf_spectacular',
    'drf_spectacular_sidecar',
    'hijack',
    'hijack.contrib.admin',
    'post_office',
    'rest_framework',
    'rest_framework_simplejwt',
]
INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'auditlog.middleware.AuditlogMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'hijack.middleware.HijackUserMiddleware',
    'django_structlog.middlewares.RequestMiddleware',
]

SITE_ID = 1

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'projeto' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

ROOT_URLCONF = 'projeto.urls'

WSGI_APPLICATION = 'projeto.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/
LANGUAGE_CODE = 'pt-br'
USE_THOUSAND_SEPARATOR = True
TIME_ZONE = 'America/Belem'
USE_I18N = True
USE_TZ = True
LOCALE_PATHS = [BASE_DIR / 'projeto' / 'locales']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/
STATIC_URL = 'assets/'
STATIC_ROOT = BASE_DIR / 'assets'
STATICFILES_DIRS = [BASE_DIR / 'projeto' / 'assets']

MEDIA_URL = 'uploads/'
MEDIA_ROOT = BASE_DIR / 'uploads'

AUTH_USER_MODEL = 'usuarios.Usuario'
LOGIN_REDIRECT_URL = '/'

AUTHENTICATION_BACKENDS = global_settings.AUTHENTICATION_BACKENDS + ['django_auth_ldap.backend.LDAPBackend']

# LDAP
# https://django-auth-ldap.readthedocs.io/en/latest/
AUTH_LDAP_SERVER_URI = env('AUTH_LDAP_SERVER_URI', default='')
AUTH_LDAP_USER_DN_TEMPLATE = env('AUTH_LDAP_USER_DN_TEMPLATE', default='')

# Task queues
# https://docs.celeryq.dev/en/stable/userguide/configuration.html
CELERY_BROKER_URL = env('BROKER_URL')
CELERY_RESULT_BACKEND = 'django-db'
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

# https://django-extensions.readthedocs.io/en/latest/graph_models.html
GRAPH_MODELS = {
    'all_applications': True,
    'group_models': True,
}

# Cache
# https://docs.djangoproject.com/en/dev/topics/cache/
CACHES = {'default': env.cache_url()}
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

# Serialization
# https://www.django-rest-framework.org/
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'projeto.apps.arquitetura.pagination.ExtraPaginator',
    'PAGE_SIZE': 15,
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',
    'DEFAULT_VERSION': 'v1',
    'ALLOWED_VERSIONS': ['v1'],
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',
                                'rest_framework.filters.SearchFilter',
                                'rest_framework.filters.OrderingFilter'),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DATETIME_FORMAT': '%Y-%m-%d',
}

# Open API
# https://drf-spectacular.readthedocs.io/en/latest/readme.html
SPECTACULAR_SETTINGS = {
    'TITLE': 'Documentação da API do Projeto',
    'DESCRIPTION': 'Descrição da API do Projeto',
    'VERSION': '0.1.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'SWAGGER_UI_DIST': 'SIDECAR',
    'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',
    'REDOC_DIST': 'SIDECAR',
}

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['*'])

# CORS Headers
# https://github.com/adamchainz/django-cors-headers
CORS_ALLOWED_ORIGINS = env.list('CORS_ALLOWED_ORIGINS', default=['http://localhost:4200'])

# Default primary key field type
# https://docs.djangoproject.com/en/dev/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'django.server': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '[{server_time}] {message}',
            'style': '{',
        },
        'json_formatter': {
            '()': structlog.stdlib.ProcessorFormatter,
            'processor': structlog.processors.JSONRenderer(),
        },
        'plain_console': {
            '()': structlog.stdlib.ProcessorFormatter,
            'processor': structlog.dev.ConsoleRenderer(),
        },
        'key_value': {
            '()': structlog.stdlib.ProcessorFormatter,
            'processor': structlog.processors.KeyValueRenderer(
                key_order=['timestamp', 'level', 'event', 'logger']
            ),
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'struct_console': {
            'class': 'logging.StreamHandler',
            'formatter': 'plain_console',
        },
        'json_file': {
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': '/var/log/gunicorn/gunicorn.json.log',
            'formatter': 'json_formatter',
        },
        'flat_line_file': {
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': '/var/log/gunicorn/gunicorn.flat_line.log',
            'formatter': 'key_value',
        },
        'celery_json_file': {
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': '/var/log/celery/celery.json.log',
            'formatter': 'json_formatter',
        },
        'celery_flat_line_file': {
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': '/var/log/celery/celery.flat_line.log',
            'formatter': 'key_value',
        },
        'django.server': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'django.server',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['struct_console', 'mail_admins'],
            'level': 'INFO',
        },
        'django.server': {
            'handlers': ['struct_console'],
            'level': 'INFO',
            'propagate': False,
        },
        'django_structlog': {
            'handlers': ['struct_console', 'flat_line_file', 'json_file'],
            'level': 'INFO',
        },
        'projeto.apps': {
            'handlers': ['struct_console', 'flat_line_file', 'json_file'],
            'level': 'INFO',
        },
        'celery':  {
            'handlers': ['struct_console', 'celery_flat_line_file', 'celery_json_file'],
            'level': 'INFO',
        },
    }
}

# Django structlog https://django-structlog.readthedocs.io/en/latest/
DJANGO_STRUCTLOG_CELERY_ENABLED = True

structlog.configure(
    processors=[
        structlog.contextvars.merge_contextvars,
        structlog.stdlib.filter_by_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
        structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
    ],
    logger_factory=structlog.stdlib.LoggerFactory(),
    cache_logger_on_first_use=True,
)
