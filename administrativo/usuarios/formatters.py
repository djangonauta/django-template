"""Formatadores da aplicação usuarios."""

from django.utils import log


class UsuarioFormatter(log.ServerFormatter):
    """Formatter que inclui o usuário na mensagem de log."""

    def format(self, record):
        """Inclui o usuário na mensagem de log."""
        record.current_user = 'Anônimo'
        request = getattr(record, 'request', None)
        if request is not None:
            record.current_user = request.user.username

        return super().format(record)
