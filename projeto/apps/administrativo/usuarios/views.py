from django import urls, shortcuts
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils import functional
from django.views import generic
from view_breadcrumbs import BaseBreadcrumbMixin

from . import models, forms


class VinculoMixin(LoginRequiredMixin, SuccessMessageMixin, BaseBreadcrumbMixin):

    def get_queryset(self):
        return models.Vinculo.objects.filter(usuario=self.request.user)

    @functional.cached_property
    def crumbs(self):
        return [('App', urls.reverse('app'))]


class VinculoSelectView(VinculoMixin, generic.FormView):

    template_name = 'usuarios/vinculo_select.html'
    form_class = forms.VinculoSelectForm
    success_url = urls.reverse_lazy('app')

    def get_initial(self):
        initial = super().get_initial()
        if 'vinculo_selecionado' in self.request.session:
            vinculo_id = self.request.session['vinculo_selecionado']['id']
            initial['vinculos'] = shortcuts.get_object_or_404(models.Vinculo, id=vinculo_id)

        return initial

    def get_form_kwargs(self):
        ctx = super().get_form_kwargs()
        ctx['request'] = self.request
        return ctx

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['vinculos'] = self.get_queryset()
        return ctx

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    @functional.cached_property
    def crumbs(self):
        lista = super().crumbs
        lista += [('Vínculos', urls.reverse('usuarios:vinculo-select'))]
        return lista


vinculo_select = VinculoSelectView.as_view()
