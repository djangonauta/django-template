from view_breadcrumbs import BaseBreadcrumbMixin
from auditlog.models import LogEntry
from django import urls
from django.contrib.auth import mixins
from django.utils import functional
from django.views import generic

from projeto.apps.arquitetura.filters import QueryParamFilterSet
from projeto.apps.arquitetura.mixins import BaseReportResponseMixin
from projeto.apps.arquitetura.views import ElidedListView


class IndexView(generic.TemplateView):

    template_name = 'index.html'


index = IndexView.as_view()


class LogEntryFilter(QueryParamFilterSet):

    class Meta:
        model = LogEntry
        fields = ['object_repr', 'action']


class AppView(mixins.LoginRequiredMixin, BaseBreadcrumbMixin, ElidedListView):

    template_name = 'app.html'
    queryset = LogEntry.objects.all()
    context_object_name = 'entries'
    paginate_by = 3
    page_kwarg = 'pagina'
    filter_class = LogEntryFilter

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
