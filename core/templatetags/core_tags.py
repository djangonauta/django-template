"""Este módulo contem tags e filtros globais em relação ao projeto."""

from hashlib import md5

from django.template import Library

register = Library()


@register.simple_tag
def gravatar_url(email):
    """Obtém a url gravatar em função do email fornecido."""
    return '//www.gravatar.com/avatar/{}'.format(md5(email.encode('utf-8')).hexdigest())
