from django import shortcuts
from django.views import generic

from projeto.apps.arquitetura.mixins import BaseReportResponseMixin


def index(request):
    return shortcuts.render(request, 'index.html', {
        'title': 'Bem vindo',
    })



class RelatorioTesteView(BaseReportResponseMixin, generic.TemplateView):

    template_name = '_reports/teste.html'

    def get_context_data(self, **kwargs):
        kwargs['mensagem'] = 'PDF WORKS'
        return super(RelatorioTesteView, self).get_context_data(**kwargs)


relatorio = RelatorioTesteView.as_view()
