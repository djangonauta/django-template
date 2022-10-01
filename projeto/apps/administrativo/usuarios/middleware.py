from django import shortcuts, urls


class VinculoMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # código pré-view
        if (request.user.is_authenticated
                and not request.session.get('vinculo', None)
                and request.path.startswith(urls.reverse('app'))):
            return shortcuts.redirect(f'/vinculos/?redirect_field={request.path}')

        response = self.get_response(request)

        # código pós-view
        return response
