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
