import hashlib
import uuid

from auditlog.models import AuditlogHistoryField
from auditlog.registry import auditlog
from django.contrib.auth.models import AbstractUser
from django.db import models
from django_prometheus.models import ExportModelOperationsMixin
from model_utils.models import TimeStampedModel

from . import managers


class Usuario(ExportModelOperationsMixin("Usuario"), TimeStampedModel, AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Tipo do usuário automaticamente definido em save()
    class Tipo(models.IntegerChoices):
        DEFAULT = 1, "default"

    tipo = models.IntegerField(choices=Tipo.choices, default=Tipo.DEFAULT)
    tipo_usuario = Tipo.DEFAULT

    history = AuditlogHistoryField()

    objects = managers.UsuarioManager()

    class Meta:
        verbose_name = "Usuário"
        db_table = 'administrativo"."usuarios_usuario'

    def save(self, *args, **kwargs):
        if not self.pk:
            self.tipo = (
                self.tipo_usuario
            )  # ao herdar da classe Usuario especificar qual o tipo de usuário

        return super().save(*args, **kwargs)

    # Métodos assim poderiam ser definidos na subclasse para verificar o tipo
    def is_default(self):
        return self.tipo == self.Tipo.DEFAULT

    @property
    def nome_completo(self):
        return self.get_full_name() or self.username

    @property
    def gravatar_url(self):
        email_hash = hashlib.md5(bytes(self.email, "utf-8")).hexdigest()
        return f"https://gravatar.com/avatar/{email_hash}"


auditlog.register(Usuario)
