"""Views da aplicação core."""

from django.contrib import auth
from django.views import generic
from rest_framework import permissions, viewsets

from . import serializers


class UserViewSet(viewsets.ModelViewSet):
    """User viewset."""

    serializer_class = serializers.UserSerializer
    permission_classes = (permissions.IsAdminUser,)
    queryset = auth.get_user_model().objects.all()


class UserInfoTemplateView(generic.TemplateView):
    """Obtém o template server side para o componente navbar."""

    template_name = 'core/user_info_template.html'
