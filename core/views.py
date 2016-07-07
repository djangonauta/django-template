"""Views da aplicação core."""

from django.contrib.auth import get_user_model
from django.views.generic import TemplateView
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from .serializers import UserSerializer


class UserViewSet(ModelViewSet):
    """User viewset."""

    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)
    queryset = get_user_model().objects.all()


class UserInfoTemplateView(TemplateView):
    """Obtém o template server side para o componente navbar."""

    template_name = 'core/user_info_template.html'
