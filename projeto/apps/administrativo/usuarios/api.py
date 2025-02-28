from django.contrib import auth
from rest_framework import permissions, viewsets
from rest_framework_simplejwt import views

from . import serializers


class UsuarioViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.UsuarioSerializer
    permission_classes = (permissions.IsAdminUser,)
    queryset = auth.get_user_model().objects.all().order_by('username')
    search_fields = ['username']


class TokenParComPermissoesView(views.TokenObtainPairView):
    serializer_class = serializers.TokenParComPermissoesSerializer
