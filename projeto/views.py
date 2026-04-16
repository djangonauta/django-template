import logging

import view_breadcrumbs
from django import shortcuts, urls
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Model
from django.utils import functional
from django.views import generic
from django_filters import CharFilter, FilterSet

from projeto.apps.administrativo.usuarios.models import Produto
from projeto.apps.arquitetura.mixins import BaseReportResponseMixin
from projeto.apps.arquitetura.views import ElidedListView

logger = logging.getLogger(__name__)


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
    descricao = CharFilter(lookup_expr="icontains")

    class Meta:
        model = Produto
        fields = ("id", "descricao", "preco")


class ProdutoListView(ElidedListView):
    model = Produto
    queryset = Produto.objects.all().order_by("-created")
    template_name = "produtos.html"
    context_object_name = "produtos"
    paginate_by = 5
    filterset_class = ProdutoFilter

    def get_template_names(self) -> list[str]:
        if self.request.headers.get("HX-Request"):
            return [self.template_name + "#produtos_partial"]

        return [self.template_name]


produto_list_view = ProdutoListView.as_view()


class ProdutoDeleteView(generic.DeleteView):
    object: Model
    model = Produto

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        messages.success(request, "Produto removido com sucesso.")
        request.method = "GET"
        return produto_list_view(request)


produto_delete_view = ProdutoDeleteView.as_view()


class CreateProdutoModalView(generic.CreateView):
    model = Produto
    template_name = "create_produto_modal.html"
    fields = ("descricao", "preco")

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Produto adicionado com sucesso.")
        return shortcuts.render(self.request, self.template_name + "#sucesso", {})


create_produto_modal = CreateProdutoModalView.as_view()


class UpdateProdutoModalView(generic.UpdateView):
    model = Produto
    template_name = "update_produto_modal.html"
    fields = ("descricao", "preco")

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Produto atualizado com sucesso.")
        return shortcuts.render(self.request, self.template_name + "#sucesso", {})


update_produto_modal = UpdateProdutoModalView.as_view()
