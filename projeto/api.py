from rest_framework import routers

from projeto.apps.administrativo.usuarios import api as usuarios_api

router = routers.DefaultRouter()
router.register("usuarios", usuarios_api.UsuarioViewSet)

urls = router.urls, "projeto", "v1"
