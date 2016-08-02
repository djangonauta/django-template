"""Core urls."""

from django.conf import urls

from . import views

urlpatterns = [
    urls.url(r'^navbar/template/$', views.UserInfoTemplateView.as_view(), name='user_info_template')
]
