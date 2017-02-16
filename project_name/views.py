"""Módulo contém views genéricas ou globais ao projeto."""

from core.serializers import UserSerializer
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from rest_framework import renderers


class IndexView(LoginRequiredMixin, generic.TemplateView):
    """
    Página base da aplicação.

    Esta página contém a infraestrutura SPA (Single Page Application): scripts, estilos, etc.
    """

    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        """Obtém o contexto da página."""
        contexto = super().get_context_data(**kwargs)
        contexto['User'] = renderers.JSONRenderer().render(UserSerializer(self.request.user).data)
        return contexto
