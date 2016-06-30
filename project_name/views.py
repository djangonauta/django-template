"""Módulo contém views genéricas ou globais ao projeto."""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class IndexView(LoginRequiredMixin, TemplateView):
    """
    Página base da aplicação.

    Esta página contém a infraestrutura SPA (Single Page Application): scripts, estilos, etc.
    """

    template_name = 'base.html'
