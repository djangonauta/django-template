from rest_framework import pagination, response, status


class ExtraPaginator(pagination.PageNumberPagination):

    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        paginator = self.page.paginator
        return response.Response({
            'count': paginator.count,
            'has_next': self.page.has_next(),
            'has_previous': self.page.has_previous(),
            'results': data,
            'page_range': list(paginator.page_range),
            'num_pages': paginator.num_pages,
            'per_page': paginator.per_page,
            'page': self.page.number,
            'next_page_number': self.page.next_page_number() if self.page.has_next() else None,
            'previous_page_number': self.page.previous_page_number() if self.page.has_previous() else None,
        }, status=status.HTTP_200_OK)
