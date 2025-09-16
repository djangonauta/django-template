from django.conf import settings
from django.conf.urls import static
from django.contrib import admin
from django.urls import include, path
from django.views import generic
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from projeto.apps.administrativo.usuarios.api import TokenParComPermissoesView

from . import api, views

urlpatterns = [
    path("", generic.RedirectView.as_view(url="app")),
    path("", include("django_prometheus.urls")),
    path("app/", views.app, name="app"),
    path("contas/", include("allauth.urls")),
    path("hijack/", include("hijack.urls")),
    path("admin/", admin.site.urls),
    path("select2/", include("django_select2.urls")),
]

# API
urlpatterns += [
    path("api/v1/", api.urls),
    path("api/token/", TokenParComPermissoesView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("api/schema.yml", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
]

# Media files in development
urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [path("__debug__/", include("debug_toolbar.urls"))]
