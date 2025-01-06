from rest_framework import pagination, response, status


class ExtraPaginator(pagination.PageNumberPagination):

    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        paginator = self.page.paginator
        return response.Response({
            'count': paginator.count,
            'has_next': self.page.has_next(),
            'has_previous': self.page.has_previous(),
            'page_range': list(paginator.page_range),
            'num_pages': paginator.num_pages,
            'per_page': paginator.per_page,
            'page': self.page.number,
            'next_page_number': self.page.next_page_number() if self.page.has_next() else None,
            'previous_page_number': self.page.previous_page_number() if self.page.has_previous() else None,
            'results': data,
        }, status=status.HTTP_200_OK)

    def get_paginated_response_schema(self, schema):
        return {
            'type': 'object',
            'properties': {
                'count': {
                    'type': 'integer',
                    'example': 15,
                },
                'has_next': {
                    'type': 'bool',
                    'example': True,
                },
                'has_previous': {
                    'type': 'bool',
                    'example': False,
                },
                'page_range': {
                    'type': 'list',
                    'example': [1, 2, 3],
                },
                'num_pages': {
                    'type': 'integer',
                    'example': 3,
                },
                'per_page': {
                    'type': 'integer',
                    'example': 5,
                },
                'page': {
                    'type': 'integer',
                    'example': 1,
                },
                'next_page_number': {
                    'type': 'integer',
                    'example': 2,
                    'nullable': True,
                },
                'previous_page_number': {
                    'type': 'integer',
                    'example': None,
                    'nullable': True,
                },
                'results': schema,
            },
        }
