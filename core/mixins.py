"""Mixins da aplicação core."""


class SelectSerializerFieldsMixin:
    """Permite redefinir campos de exibição de um serializador."""

    def __init__(self, *args, selected_field_names=None, **kwargs):
        """
        Atualiza os campos deste serializador.

        A variável selected_field_names é uma lista de campos selecionados para este serializador.
        """
        super(SelectSerializerFieldsMixin, self).__init__(*args, **kwargs)
        if selected_field_names is not None:
            original_field_names = self.fields.keys()

            # Remove os campos que não foram selecionados.
            for field_name in original_field_names - selected_field_names:
                self.fields.pop(field_name)
