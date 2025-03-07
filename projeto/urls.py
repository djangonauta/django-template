from django import urls
from django.conf import settings
from django.conf.urls import static
from django.contrib import admin
from django.views import generic
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from projeto.apps.administrativo.usuarios.api import TokenParComPermissoesView

from . import api, views

urlpatterns = [
    urls.path('', generic.RedirectView.as_view(url='app')),
    urls.path('', urls.include('django_prometheus.urls')),
    urls.path('app/', views.app, name='app'),
    urls.path('erro/', views.erro, name='erro'),
    urls.path('contas/', urls.include('allauth.urls')),
    urls.path('hijack/', urls.include('hijack.urls')),
    urls.path('admin/', admin.site.urls),
    urls.path('select2/', urls.include('django_select2.urls')),
]

# API
urlpatterns += [
    urls.path('api/v1/', api.urls),
    urls.path('api/token/', TokenParComPermissoesView.as_view(), name='token_obtain_pair'),
    urls.path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    urls.path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    urls.path('api/schema.yml', SpectacularAPIView.as_view(), name='schema'),
    urls.path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]

# Media files in development
urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [urls.path('__debug__/', urls.include('debug_toolbar.urls'))]
