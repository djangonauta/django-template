import view_breadcrumbs
from django import forms, shortcuts, urls
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.utils import functional
from django.views import generic
from django_celery_results.models import TaskResult

from projeto.apps.arquitetura import tasks
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


class MensagemForm(forms.Form):

    mensagem = forms.CharField()

    def save(self, *args, **kwargs):
        return tasks.email_admins_teste.delay(self.cleaned_data['mensagem'])


class IndexView(BaseBreadcrumbMixin, LoginRequiredMixin, generic.FormView):

    template_name = 'index.html'
    titulo_pagina = 'Home'
    form_class = MensagemForm
    success_url = '/'

    def form_valid(self, form):
        self.request.session['task_id'] = form.save().id
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        if 'task_id' in self.request.session:
            condicao = Q(task_id=self.request.session['task_id'])
            if TaskResult.objects.filter(condicao).exists():
                kwargs['resultado'] = TaskResult.objects.get(condicao)

        return super().get_context_data(**kwargs)


index = IndexView.as_view()


class LimparResultado(generic.View):

    def post(self, *args, **kwargs):
        if 'task_id' in self.request.session:
            del self.request.session['task_id']

        return shortcuts.redirect('/')


limpar_resultado = LimparResultado.as_view()


def erro(request):
    return 1 / 0


class RelatorioTesteView(BaseReportResponseMixin, generic.TemplateView):

    template_name = '_reports/teste.html'

    def get_context_data(self, **kwargs):
        kwargs['mensagem'] = 'PDF WORKS'
        return super().get_context_data(**kwargs)


relatorio = RelatorioTesteView.as_view()
