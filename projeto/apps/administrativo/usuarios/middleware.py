from django import shortcuts, urls


class VinculoMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # código pré-view
        if (request.user.is_authenticated  # se usuário está autenticado
                and request.path.startswith(urls.reverse('app'))  # acessando a aplicação
                and not request.session.get('vinculo', None)):  # sem vínculo selecionado
            # redirecionar para página de seleção de vínculo
            return shortcuts.redirect(f'/vinculos/?redirect_field={request.path_info}')

        response = self.get_response(request)

        # código pós-view
        return response
