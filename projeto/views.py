import view_breadcrumbs
from django import urls
from django.contrib.auth import mixins
from django.utils import functional
from django.views import generic

from projeto.apps.arquitetura.mixins import BaseReportResponseMixin


class IndexView(generic.TemplateView):

    template_name = 'index.html'


index = IndexView.as_view()


class AppView(mixins.LoginRequiredMixin, view_breadcrumbs.BaseBreadcrumbMixin, generic.TemplateView):

    template_name = 'app.html'

    @functional.cached_property
    def crumbs(self):
        return [('App', urls.reverse('app'))]


app = AppView.as_view()


class RelatorioTesteView(BaseReportResponseMixin, generic.TemplateView):

    template_name = '_reports/teste.html'

    def get_context_data(self, **kwargs):
        kwargs['mensagem'] = 'PDF WORKS'
        return super().get_context_data(**kwargs)


relatorio = RelatorioTesteView.as_view()
