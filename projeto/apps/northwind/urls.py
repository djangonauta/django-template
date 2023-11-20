from django import urls
from django.views import generic

app_name = 'projeto.apps.northwind'

urlpatterns = [
    urls.path('', generic.TemplateView.as_view(template_name='northwind/index.html'), name='index'),
]
