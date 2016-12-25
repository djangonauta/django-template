"""Storages para uso com Amazon S3."""

from django.conf import settings
from storages.backends.s3boto import S3BotoStorage


class MediaLocationStorage(S3BotoStorage):
    """Storage para arquivos de mídia."""

    location = settings.MEDIAFILES_LOCATION
