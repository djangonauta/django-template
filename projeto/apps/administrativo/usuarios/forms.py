from django import forms

from . import models, serializers


class VinculoSelectForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)

        vinculos_usuario = models.Vinculo.objects.filter(usuario=self.request.user)
        self.fields['vinculos'] = forms.ModelChoiceField(vinculos_usuario, widget=forms.RadioSelect(
            attrs={'class': 'form-check-input'}
        ))

    def save(self, *args, **kwargs):
        vinculo_data = serializers.VinculoSerializer(self.cleaned_data['vinculos']).data
        self.request.session['vinculo_selecionado'] = vinculo_data
