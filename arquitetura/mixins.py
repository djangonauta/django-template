"""Mixins da aplicação arquitetura."""

from rest_framework import response, status


class SelectSerializerFieldsMixin:
    """Permite redefinir campos de exibição de um serializador."""

    param_field_names = 'field_names'

    def to_representation(self, data):
        """Seleciona os campos de exibição em função de parâmetros da solicitação."""
        data = super(SelectSerializerFieldsMixin, self).to_representation(data)
        fields = self.context['request'].query_params.get(self.param_field_names, None)
        if fields:
            fields = set(fields.split(','))
            data = {k: v for k, v in data.items() if k in fields}

        return data


class PaginatedResponseMixin:
    """Mixin para respostas paginadas."""

    def build_paginated_response(self, objects):
        """Obtém a resposta paginada quando possível."""
        page = self.paginate_queryset(objects)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(objects, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)
