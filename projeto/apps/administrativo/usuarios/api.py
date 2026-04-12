from django.contrib import auth
from django.db.models import Case, Q, Value, When
from django.db.models.functions import Concat
from rest_framework import permissions, viewsets
from rest_framework_simplejwt import views

from . import serializers


class UsuarioViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.UsuarioSerializer
    permission_classes = (permissions.IsAdminUser,)
    queryset = auth.get_user_model().objects.all()
    search_fields = ("username", "nome_completo")

    def get_queryset(self):
        nome_completo = Case(
            When(Q(first_name="") & Q(last_name=""), then="username"),
            default=Concat("first_name", Value(" "), "last_name"),
        )
        qs = auth.get_user_model().objects
        return qs.annotate(nome_completo=nome_completo).all().order_by("username")


class TokenParComPermissoesView(views.TokenObtainPairView):
    serializer_class = serializers.TokenParComPermissoesSerializer
