# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/
from .staging import *  # noqa: F401, F403


STATIC_ROOT = BASE_DIR / '..' / 'assets'  # noqa: F405
MEDIA_ROOT = BASE_DIR / '..' / 'downloads'  # noqa: F405

# Security
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_SECONDS = 15_638_400
SECURE_HSTS_PRELOAD = True
SECURE_REDIRECT_EXEMPT = []
SECURE_SSL_HOST = None
SECURE_SSL_REDIRECT = env.bool('SECURE_SSL_REDIRECT', default=False)  # noqa f405
CSRF_COOKIE_HTTPONLY = False
X_FRAME_OPTIONS = 'DENY'
