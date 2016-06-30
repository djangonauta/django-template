"""Módulo de configuração de urls do projeto."""

from core.views import UserViewSet
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib.admin import site
from rest_framework.routers import DefaultRouter

from .views import IndexView

router = DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^contas/', include('allauth.urls')),
    url(r'^rest_auth/', include('rest_auth.urls')),
    url(r'^api/v1/', include(router.urls, namespace='v1')),
    url(r'^admin/', include(site.urls)),
]

# media files in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
