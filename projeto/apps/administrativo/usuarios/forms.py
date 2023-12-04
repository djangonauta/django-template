from django import forms
from django.core import exceptions

from . import models


class VinculoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        return super().__init__(*args, **kwargs)

    class Meta:
        model = models.Vinculo
        fields = ['unidade', 'responsabilidade']

    def vinculo_existe(self):
        data = self.cleaned_data
        kwargs = dict(
            usuario=self.request.user,
            unidade=data.get('unidade'),
            responsabilidade=data.get('responsabilidade')
        )
        if all(kwargs.values()):
            return models.Vinculo.objects.filter(**kwargs).exists()

        return False

    def clean(self):
        if self.vinculo_existe():
            raise exceptions.ValidationError('Vínculo com os dados informados já existe')

        return super().clean()
