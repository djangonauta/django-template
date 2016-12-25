"""Core utils."""

from os import path


def get_path_from_dir(path_, from_):
    """Obtém path a partir do diretório de from_."""
    return path.abspath(path.join(path.dirname(from_), path_))
