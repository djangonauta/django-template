"""Módulo de configuração de urls do projeto."""

from django import urls
from django.conf import settings
from django.conf.urls import static
from django.contrib import admin

from rest_framework import documentation

from . import api, views

urlpatterns = [
    urls.re_path(r'^$', views.index, name='index'),
    urls.re_path(r'^contas/', urls.include('allauth.urls')),
    urls.re_path(r'^api/v1/', api.urls),
    urls.re_path(r'^api-auth/', urls.include('rest_framework.urls', namespace='rest_framework')),
    urls.re_path(r'^admin/', admin.site.urls),
    urls.re_path(r'^docs/', documentation.include_docs_urls(title='Documentação funcional da API')),
]

# media files in development
urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        urls.re_path(r'^__debug__/', urls.include(debug_toolbar.urls))
    ]
