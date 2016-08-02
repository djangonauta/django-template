"""wsgi module."""

import os

from django.core import wsgi

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings")
application = wsgi.get_wsgi_application()
