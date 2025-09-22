import hashlib
import uuid

from auditlog.models import AuditlogHistoryField
from auditlog.registry import auditlog
from django.contrib.auth.models import AbstractUser
from django.db.models import IntegerField, UUIDField
from django_prometheus.models import ExportModelOperationsMixin
from model_utils.models import TimeStampedModel

from .managers import TipoUsuario, UsuarioManager


class Usuario(ExportModelOperationsMixin("Usuario"), TimeStampedModel, AbstractUser):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tipo = IntegerField(choices=TipoUsuario.choices, default=TipoUsuario.DEFAULT)

    history = AuditlogHistoryField()
    objects = UsuarioManager()

    class Meta:
        verbose_name = "Usuário"
        db_table = 'administrativo"."usuarios_usuario'

    def is_default(self) -> bool:
        return self.tipo == TipoUsuario.DEFAULT

    @property
    def nome_completo(self) -> str:
        return self.get_full_name() or self.username

    @property
    def gravatar_url(self) -> str:
        email_hash = hashlib.md5(bytes(self.email, "utf-8")).hexdigest()
        return f"https://gravatar.com/avatar/{email_hash}"


auditlog.register(Usuario)
