from django.views import generic

from projeto.apps.arquitetura.mixins import BaseReportResponseMixin


class IndexView(generic.TemplateView):

    template_name = 'index.html'


index = IndexView.as_view()


class RelatorioTesteView(BaseReportResponseMixin, generic.TemplateView):

    template_name = '_reports/teste.html'

    def get_context_data(self, **kwargs):
        kwargs['mensagem'] = 'PDF WORKS'
        return super().get_context_data(**kwargs)


relatorio = RelatorioTesteView.as_view()
