"""Rotas da API."""

from rest_framework import routers

from core.views import UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)

urls = router.urls, 'controle_ponto', 'v1'
