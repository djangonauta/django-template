"""Módulo contém views genéricas ou globais ao projeto."""

from django.contrib.auth import mixins
from django.views import generic


class IndexView(mixins.LoginRequiredMixin, generic.TemplateView):
    """
    Página base da aplicação.

    Esta página contém a infraestrutura SPA (Single Page Application): scripts, estilos, etc.
    """

    template_name = 'base.html'
