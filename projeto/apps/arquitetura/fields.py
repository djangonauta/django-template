"""https://docs.djangoproject.com/en/dev/topics/http/file-uploads/#uploading-multiple-files

 def form_valid(self, form):
        files = form.cleaned_data["file_field"]
        for f in files:
            ...  # Do something with each file.
        return super().form_valid()
"""
from django import forms


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('widget', MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        if isinstance(data, (list, tuple)):
            return [super().clean(d, initial) for d in data]

        return super().clean(data, initial)


class InputDateField(forms.DateField):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('widget', forms.DateInput(format='%Y-%m-%d')).input_type = 'date'
        super().__init__(*args, **kwargs)


class ModelMultipleChoiceFieldCheckbox(forms.ModelMultipleChoiceField):

    def __init__(self, *args, **kwargs):
        attrs = {'class': 'form-check-input ponteiro'}
        kwargs.setdefault('widget', forms.CheckboxSelectMultiple(attrs=attrs))
        super().__init__(*args, **kwargs)


class ModelChoiceFieldRadio(forms.ModelChoiceField):

    def __init__(self, *args, **kwargs):
        attrs = {'class': 'form-check-input ponteiro'}
        kwargs.setdefault('widget', forms.RadioSelect(attrs=attrs))
        super().__init__(*args, **kwargs)
