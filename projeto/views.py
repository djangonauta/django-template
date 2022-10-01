from django import forms
from django.contrib.auth import mixins
from django.db import models
from django.views import generic

from projeto.apps.arquitetura.mixins import BaseReportResponseMixin


class IndexView(generic.TemplateView):

    template_name = 'index.html'


index = IndexView.as_view()


class AppView(mixins.LoginRequiredMixin, generic.TemplateView):

    template_name = 'app.html'


app = AppView.as_view()


class VinculoForm(forms.Form):

    class VinculoOptions(models.IntegerChoices):
        PRIMARIO = 1, 'Primário'
        SECUNDARIO = 2, 'Secundário'

    vinculo = forms.ChoiceField(choices=VinculoOptions.choices)
    redirect_field = forms.CharField(max_length=255)

    def salvar_vinculo(self, request):
        request.session['vinculo'] = self.cleaned_data['vinculo']


class VinculosView(mixins.LoginRequiredMixin, generic.FormView):

    form_class = VinculoForm
    template_name = 'vinculos.html'

    def form_valid(self, form):
        form.salvar_vinculo(self.request)
        self.success_url = form.cleaned_data['redirect_field']
        return super().form_valid(form)

    def get_context_data(self):
        ctx = super().get_context_data()
        ctx['redirect_field'] = self.request.GET.get('redirect_field', '/')
        return ctx


vinculos = VinculosView.as_view()


class RelatorioTesteView(BaseReportResponseMixin, generic.TemplateView):

    template_name = '_reports/teste.html'

    def get_context_data(self, **kwargs):
        kwargs['mensagem'] = 'PDF WORKS'
        return super().get_context_data(**kwargs)


relatorio = RelatorioTesteView.as_view()
