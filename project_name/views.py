"""Módulo contém views genéricas ou globais ao projeto."""

from django.views import generic


class IndexView(generic.TemplateView):
    """
    Página base da aplicação.

    Esta página contém a infraestrutura SPA (Single Page Application): scripts, estilos, etc.
    """

    template_name = 'base.html'
