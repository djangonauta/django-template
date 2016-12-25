"""Módulo de configuração de urls do projeto."""

import os

from core import views as core_views
from django.conf import settings, urls
from django.conf.urls import static
from django.contrib import admin
from django.contrib.auth.views import password_reset_complete, password_reset_confirm
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from . import views

router = routers.DefaultRouter()
router.register('users', core_views.UserViewSet)

urlpatterns = [
    urls.url(r'^$', views.IndexView.as_view(), name='home'),
    urls.url(r'^rest_auth/', urls.include('rest_auth.urls')),
    urls.url(r'^rest_auth/registration/', urls.include('rest_auth.registration.urls')),
    urls.url(r'^contas/', urls.include('allauth.urls')),
    urls.url(r'^api/v1/', urls.include(router.urls, namespace='v1')),
    urls.url(r'^api-auth/', urls.include('rest_framework.urls', namespace='rest_framework')),
    urls.url(r'^core/', urls.include('core.urls', namespace='core')),
    urls.url(r'^admin/', urls.include(admin.site.urls)),
]

# auth urls utilizadas pelo rest_auth
urlpatterns += [
    urls.url(r'^contas/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
             password_reset_confirm, name='password_reset_confirm'),
    urls.url(r'^contas/reset/done/$', password_reset_complete, name='password_reset_complete'),
]

# media files in development
urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG or 'heroku' in os.environ.get('DJANGO_SETTINGS_MODULE'):
    import debug_toolbar
    urlpatterns += [
        urls.url(r'^__debug__/', urls.include(debug_toolbar.urls)),
        urls.url(r'^schema/$', get_swagger_view(title='{{ project_name }}')),
    ]
