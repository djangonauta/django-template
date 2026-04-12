import view_breadcrumbs
from django import urls
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import functional
from django.views import generic
from django_filters import FilterSet

from projeto.apps.administrativo.usuarios.models import Produto
from projeto.apps.arquitetura.mixins import BaseReportResponseMixin
from projeto.apps.arquitetura.views import ElidedListView


class BaseBreadcrumbMixin(view_breadcrumbs.BaseBreadcrumbMixin):
    titulo_pagina: str

    def get_context_data(self, **kwargs):
        kwargs["titulo_pagina"] = self.titulo_pagina
        return super().get_context_data(**kwargs)

    @functional.cached_property
    def crumbs(self):
        return [("Home", urls.reverse("app"))]


class AppView(BaseBreadcrumbMixin, LoginRequiredMixin, generic.TemplateView):
    template_name = "app.html"
    titulo_pagina = "Home"
    success_url = "/"


app = AppView.as_view()


class RelatorioTesteView(BaseReportResponseMixin, generic.TemplateView):
    template_name = "_reports/teste.html"

    def get_context_data(self, **kwargs):
        kwargs["mensagem"] = "PDF WORKS"
        return super().get_context_data(**kwargs)


relatorio = RelatorioTesteView.as_view()


class ProdutoFilter(FilterSet):
    class Meta:
        model = Produto
        fields = ("id", "descricao", "preco")


class ProdutoListView(ElidedListView):
    model = Produto
    template_name = "produtos.html"
    context_object_name = "produtos"
    paginate_by = 5
    filterset_class = ProdutoFilter

    def get_template_names(self) -> list[str]:
        if self.request.headers.get("HX-Request"):
            return [self.template_name + "#produtos_table"]

        return [self.template_name]


produto_list_view = ProdutoListView.as_view()
