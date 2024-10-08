from django import urls
from django.conf import settings
from django.conf.urls import static
from django.contrib import admin
from django.views import generic
from rest_framework import documentation
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from . import api, views

urlpatterns = [
    urls.path('', generic.RedirectView.as_view(url='app')),
    urls.path('app/', views.app, name='app'),
    urls.path('contas/', urls.include('allauth.urls')),
    urls.path('hijack/', urls.include('hijack.urls')),
    urls.path('admin/', admin.site.urls),
    urls.path('docs/', documentation.include_docs_urls(title='Documentação funcional da API')),
]

# API
urlpatterns += [
    urls.path('api/v1/', api.urls),
    urls.path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    urls.path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    urls.path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

# Media files in development
urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [urls.path('__debug__/', urls.include('debug_toolbar.urls'))]
