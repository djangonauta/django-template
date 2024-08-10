from django import urls
from django.conf import settings
from django.conf.urls import static
from django.contrib import admin
from rest_framework import documentation

from . import api, views

urlpatterns = [
    urls.path('', views.index, {'mensagem': 'kwargs'}, name='index'),
    urls.path('app/', views.index, name='app'),
    urls.path('limpar/resultado/', views.limpar_resultado, name='limpar-resultado'),
    urls.path('report/', views.relatorio, name='report'),  # remover
    urls.path('contas/', urls.include('allauth.urls')),
    urls.path('hijack/', urls.include('hijack.urls')),
    urls.path('api/v1/', api.urls),
    # urls.path('api-auth/', urls.include('rest_framework.urls', namespace='rest_framework')),
    urls.path('admin/', admin.site.urls),
    urls.path('docs/', documentation.include_docs_urls(title='Documentação funcional da API')),
    urls.path('erro/', views.erro, name='erro'),  # remover
]

# media files in development
urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [urls.path('__debug__/', urls.include('debug_toolbar.urls'))]
