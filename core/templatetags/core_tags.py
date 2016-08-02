"""Este módulo contem tags e filtros globais em relação ao projeto."""

import hashlib

from django import template

register = template.Library()


@register.simple_tag
def gravatar_url(email):
    """Obtém a url gravatar em função do email fornecido."""
    return '//www.gravatar.com/avatar/{}'.format(hashlib.md5(email.encode('utf-8')).hexdigest())
