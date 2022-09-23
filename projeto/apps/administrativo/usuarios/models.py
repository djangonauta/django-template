import hashlib
import os.path

from auditlog.models import AuditlogHistoryField
from auditlog.registry import auditlog
from django.contrib.auth.models import AbstractUser
from django.db import models
from model_utils.models import TimeStampedModel


def diretorio_imagem_perfil(instance, filename):
    return os.path.join(instance.username, 'imagem-perfil', filename)


class Usuario(TimeStampedModel, AbstractUser):

    class Meta:
        verbose_name = 'Usuário'
        db_table = 'administrativo\".\"usuarios_usuario'

    imagem_perfil = models.ImageField(upload_to=diretorio_imagem_perfil, null=True, blank=True)

    history = AuditlogHistoryField()

    def gravatar_url(self):
        email_hash = hashlib.md5(self.email.encode('utf-8')).hexdigest()
        return f'//www.gravatar.com/avatar/{email_hash}'

    def perfil_imagem(self):
        return self.imagem_perfil.url if self.imagem_perfil else self.gravatar_url()

    def nome_completo(self):
        return self.get_full_name() or self.username


auditlog.register(Usuario)
