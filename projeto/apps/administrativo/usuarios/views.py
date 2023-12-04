from django import urls
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils import functional
from django.views import generic
from view_breadcrumbs import BaseBreadcrumbMixin

from . import forms, models


class VinculoBreadcrumbMixin(LoginRequiredMixin, SuccessMessageMixin, BaseBreadcrumbMixin):

    def get_queryset(self):
        return models.Vinculo.objects.filter(usuario=self.request.user)

    @functional.cached_property
    def crumbs(self):
        return [('App', urls.reverse('app')), ('Vínculos', urls.reverse('usuarios:vinculo-create'))]


class VinculoCreateView(VinculoBreadcrumbMixin, generic.CreateView):

    template_name = 'usuarios/vinculo_create.html'
    form_class = forms.VinculoForm
    success_message = 'Vínculo criado com sucesso'
    success_url = urls.reverse_lazy('usuarios:vinculo-create')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.usuario = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['vinculos'] = self.get_queryset()
        return ctx


vinculo_create = VinculoCreateView.as_view()


class VinculoUpdateView(VinculoCreateView, generic.UpdateView):

    success_message = 'Vínculo atualizado com sucesso'


vinculo_update = VinculoUpdateView.as_view()


class VinculoDeleteView(VinculoBreadcrumbMixin, generic.DeleteView):

    template_name = 'usuarios/vinculo_delete.html'
    success_message = 'Vínculo %(str)s removido com sucesso'
    success_url = urls.reverse_lazy('usuarios:vinculo-create')

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, str=str(self.object))

    @functional.cached_property
    def crumbs(self):
        lista = super().crumbs
        lista += [('Remover', urls.reverse('usuarios:vinculo-delete', args=(self.object.pk,)))]
        return lista


vinculo_delete = VinculoDeleteView.as_view()
