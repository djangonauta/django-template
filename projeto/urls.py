from django import urls
from django.conf import settings
from django.conf.urls import static
from django.contrib import admin
from rest_framework import documentation

from . import api, views

urlpatterns = [
    urls.path('', views.index, {'mensagem': 'kwargs'}, name='index'),
    urls.path('app/', views.app, name='app'),
    urls.path('usuarios/', urls.include('projeto.apps.administrativo.usuarios.urls', namespace='usuarios')),  # noqa: E501
    urls.path('report/', views.relatorio, name='report'),  # remover
    urls.path('contas/', urls.include('allauth.urls')),
    urls.path('hijack/', urls.include('hijack.urls', namespace='hijack')),
    urls.path('api/v1/', api.urls),
    # urls.path('api-auth/', urls.include('rest_framework.urls', namespace='rest_framework')),
    urls.path('admin/', admin.site.urls),
    urls.path('docs/', documentation.include_docs_urls(title='Documentação funcional da API')),
]

# media files in development
urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [urls.path('__debug__/', urls.include('debug_toolbar.urls'))]
