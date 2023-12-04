from auditlog.models import AuditlogHistoryField
from auditlog.registry import auditlog
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from model_utils.models import TimeStampedModel

from . import managers


class Usuario(TimeStampedModel, AbstractUser):

    # Tipo do usuário automaticamente definido em save()
    class Tipo(models.IntegerChoices):
        DEFAULT = 1,  'default'

    tipo = models.IntegerField(choices=Tipo.choices, default=Tipo.DEFAULT)
    tipo_usuario = Tipo.DEFAULT

    history = AuditlogHistoryField()

    objects = managers.UsuarioManager()

    class Meta:
        verbose_name = 'Usuário'
        db_table = 'administrativo\".\"usuarios_usuario'

    def save(self, *args, **kwargs):
        if not self.pk:
            self.tipo = self.tipo_usuario  # ao herdar da classe Usuario especificar qual o tipo de usuário

        return super().save(*args, **kwargs)

    # Métodos assim poderiam ser definidos na subclasse para verificar o tipo
    def is_default(self):
        return self.tipo == self.Tipo.DEFAULT

    @property
    def nome_completo(self):
        return self.get_full_name() or self.username


auditlog.register(Usuario)


class Unidade(TimeStampedModel):

    nome = models.CharField(max_length=255)
    codigo = models.CharField(max_length=255)
    hierarquia = models.CharField(max_length=255)

    history = AuditlogHistoryField()

    def __str__(self):
        return f'{self.nome} ({self.codigo})'


auditlog.register(Unidade)


class Vinculo(TimeStampedModel):

    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='vinculos')
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE, related_name='vinculos')

    class Responsabilidade(models.TextChoices):
        CH = 'CH', 'Chefe'
        VC = 'VC', 'Vice Chefe'
        SC = 'SC', 'Secretaria'
        SE = 'SE', 'Servidor'

    responsabilidade = models.CharField(max_length=2, choices=Responsabilidade.choices, default='SE')

    history = AuditlogHistoryField()

    def __str__(self):
        return f'{self.usuario.nome_completo} - {self.unidade}'


auditlog.register(Vinculo)
