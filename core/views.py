"""Views da aplicação core."""

from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from .serializers import UserSerializer


class UserViewSet(ModelViewSet):
    """User viewset."""

    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)
    queryset = get_user_model().objects.all()
