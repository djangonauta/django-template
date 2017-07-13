"""Adaptadores da aplicação core."""

from allauth.account import adapter


class DisableSignupAdapter(adapter.DefaultAccountAdapter):
    """Adaptador para contas."""

    def is_open_for_signup(self, request):
        """Desativa o processo de registro."""
        return False
