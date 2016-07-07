"""Core urls."""

from django.conf.urls import url

from .views import UserInfoTemplateView

urlpatterns = [
    url(r'^navbar/template/$', UserInfoTemplateView.as_view(), name='user_info_template')
]
