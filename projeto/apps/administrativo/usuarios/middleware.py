from django import shortcuts, urls
from django.conf import settings


class VinculoSelectMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        acesso_aplicacao = request.path_info.startswith(f'/{settings.APP_CONTEXT}')
        vinculo_foi_selecionado = 'vinculo_selecionado' in request.session

        if acesso_aplicacao and not vinculo_foi_selecionado:
            return shortcuts.redirect(urls.reverse('vinculo-select'))

        response = self.get_response(request)
        return response
