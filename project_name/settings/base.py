"""Configurações gerais do projeto {{ project_name }}."""

import environ
from django.conf import global_settings
from django.core import urlresolvers

root = environ.Path(__file__) - 3
env = environ.Env(DEBUG=(bool, True))
environ.Env.read_env()

# Build paths inside the {{ project_name }} like this: join(BASE_DIR, ...)
BASE_DIR = root()


def get_name_email(value):
    """Helper para obter nome e email de admins e/ou managers da aplicação."""
    result = []
    for token in value.split(':'):
        name, email = token.split(',')
        result.append((name, email))

    return result


# export ADMINS=username1,email1@domain.com:username2,email2@domain.com
ADMINS = get_name_email(env('ADMINS'))
managers = env('MANAGERS', default=None)
MANAGERS = get_name_email(managers) if managers else ADMINS


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {'default': env.db()}
DATABASES['default']['ATOMIC_REQUESTS'] = True

# Email
# https://docs.djangoproject.com/en/dev/topics/email/
env.DB_SCHEMES.update(postoffice='post_office.EmailBackend')
vars().update(env.email_url())

DEFAULT_CHARSET = env('DEFAULT_CHARSET', default='utf-8')  # default charset in django.core.email.
# default from_email in EmailMessage.
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL', default='webmaster@localhost')
# default prefix + subject in mail_admins/managers.
EMAIL_SUBJECT_PREFIX = env('EMAIL_SUBJECT_PREFIX', default='[Django]')
# default from: header in mail_admins/managers.
SERVER_EMAIL = env('SERVER_EMAIL', default='admin@localhost')

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_assets',
    'core.apps.CoreConfig',
    'gunicorn',
    'post_office',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_swagger',
    'allauth',
    'allauth.account',
    'rest_auth',
    'rest_auth.registration',
    'widget_tweaks',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

SITE_ID = 1

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [root.path('{{ project_name }}')('templates')],
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

ROOT_URLCONF = '{{ project_name }}.urls'

WSGI_APPLICATION = '{{ project_name }}.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/
LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = root.path('')('static')
STATICFILES_DIRS = (root.path('{{ project_name }}')('static'),)
STATICFILES_FINDERS = global_settings.STATICFILES_FINDERS + ['django_assets.finders.AssetsFinder']
ASSETS_ROOT = root.path('{{ project_name }}')('static')
UGLIFYJS_EXTRA_ARGS = ['--compress', '--mangle']

MEDIA_URL = '/media/'
MEDIA_ROOT = root.path('')('media')

AUTH_USER_MODEL = 'core.User'
LOGIN_URL = urlresolvers.reverse_lazy('account_login')
LOGOUT_URL = urlresolvers.reverse_lazy('account_logout')
LOGIN_REDIRECT_URL = '/'

ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 7
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = ''
if env('DISABLE_ACCOUNT_REGISTRATION', default=False):
    ACCOUNT_ADAPTER = 'core.adapters.DisableSignupAdapter'
    REST_AUTH_REGISTER_SERIALIZERS = {
        'REGISTER_SERIALIZER': 'core.serializers.DisableSignupSerializer'
    }

OLD_PASSWORD_FIELD_ENABLED = True

CELERY_TASK_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['pickle', 'json']

CACHES = {'default': env.cache()}

ALLOWED_HOSTS = ['*']
INTERNAL_IPS = ['127.0.0.1']
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

AUTHENTICATION_BACKENDS = global_settings.AUTHENTICATION_BACKENDS + \
    ['allauth.account.auth_backends.AuthenticationBackend']

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 15,
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',
                                'rest_framework.filters.SearchFilter',
                                'rest_framework.filters.OrderingFilter')
}

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
            'format': '[%(server_time)s] %(message)s',
        },
        'ttcc': {
            'class': 'core.formatters.UserFormatter',
            'datefmt': '%d/%b/%Y %H:%M:%S',
            'format': '[%(server_time)s] %(levelname)s %(current_user)s %(message)s',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'console_ttcc': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'ttcc',
        },
        'file_ttcc': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'filename': root.path('')('production.log'),
            'formatter': 'ttcc',
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
            'handlers': ['console', 'mail_admins'],
            'level': 'INFO',
        },
        'django.server': {
            'handlers': ['django.server'],
            'level': 'INFO',
            'propagate': False,
        },
        'core': {
            'handlers': ['console_ttcc', 'file_ttcc'],
            'level': 'DEBUG',
        },
    }
}
