"""Módulo de configuração de urls do projeto."""

from core import views as core_views
from django.conf import settings, urls
from django.conf.urls import static
from django.contrib import admin
from rest_framework import routers

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

# media files in development
urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [urls.url(r'^__debug__/', urls.include(debug_toolbar.urls))]
