from django import forms

from projeto.apps.arquitetura import fields, mixins

from . import models, serializers


class VinculoSelectForm(mixins.RequestFormMixin, forms.Form):

    redirect_url = forms.CharField(widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        vinculos_usuario = models.Vinculo.objects.filter(usuario=self.request.user)
        self.fields['vinculos'] = fields.ModelChoiceFieldRadio(
            vinculos_usuario,
            error_messages=dict(required='É necessário escolher algum dos vínculos disponíveis'),
        )

    def save(self, *args, **kwargs):
        vinculo_data = serializers.VinculoSerializer(self.cleaned_data['vinculos']).data
        self.request.session['vinculo_selecionado'] = vinculo_data
