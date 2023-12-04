from django import urls

from . import views

app_name = 'administrativo.usuarios'

urlpatterns = [
    urls.path('vinculos/', views.vinculo_create, name='vinculo-create'),
    urls.path('vinculos/<int:pk>/', views.vinculo_update, name='vinculo-update'),
    urls.path('vinculos/<int:pk>/remover/', views.vinculo_delete, name='vinculo-delete'),
]
