from django import urls

from . import views

app_name = 'usuarios'

urlpatterns = [
    urls.path('vinculos/selecionar/', views.vinculo_select, name='vinculo-select'),
]
