import view_breadcrumbs
from django import urls
from django.contrib import messages
from django.utils import functional
from django.views import generic

from projeto.apps.arquitetura.mixins import BaseReportResponseMixin


class BaseBreadcrumbMixin(view_breadcrumbs.BaseBreadcrumbMixin):

    def get_context_data(self, **kwargs):
        kwargs['titulo_pagina'] = self.titulo_pagina
        return super().get_context_data(**kwargs)

    @functional.cached_property
    def crumbs(self):
        return [
            ('Home', urls.reverse('index')),
        ]


class IndexView(BaseBreadcrumbMixin, generic.TemplateView):

    template_name = 'index.html'
    titulo_pagina = 'Home'

    def get_context_data(self, **kwargs):
        messages.add_message(self.request, messages.INFO, 'Mensagens configuradas')
        messages.add_message(self.request, messages.SUCCESS, 'Mensagem de sucesso')
        return super().get_context_data(**kwargs)


index = IndexView.as_view()


def erro(request):
    return 1 / 0


class RelatorioTesteView(BaseReportResponseMixin, generic.TemplateView):

    template_name = '_reports/teste.html'

    def get_context_data(self, **kwargs):
        kwargs['mensagem'] = 'PDF WORKS'
        return super().get_context_data(**kwargs)


relatorio = RelatorioTesteView.as_view()
