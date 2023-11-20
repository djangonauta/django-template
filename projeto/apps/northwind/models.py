from auditlog.models import AuditlogHistoryField
from auditlog.registry import auditlog
from django.db import models
from model_utils.models import TimeStampedModel


class Fornecedor(TimeStampedModel):

    nome = models.CharField(max_length=255)
    history = AuditlogHistoryField()

    class Meta:

        verbose_name_plural = 'fornecedores'

    def __str__(self):
        return self.nome


auditlog.register(Fornecedor)


class Categoria(TimeStampedModel):

    nome = models.CharField(max_length=255)
    history = AuditlogHistoryField()

    def __str__(self):
        return self.nome


auditlog.register(Categoria)


class Produto(TimeStampedModel):

    fornecedor = models.ForeignKey(Fornecedor, related_name='produtos', on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria, related_name='produtos')

    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=9, decimal_places=2)
    history = AuditlogHistoryField()

    def __str__(self):
        return f'{self.nome} (R$ {self.preco})'


auditlog.register(Produto)


class Cliente(TimeStampedModel):

    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Compra(TimeStampedModel):

    cliente = models.ForeignKey(Cliente, related_name='compras', on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Produto, related_name='compras', through='DetalheCompra')

    data = models.DateField()

    @property
    def total(self):
        return sum(d.preco * d.quantidade for d in self.detalhe_compra.all())

    def __str__(self):
        return f'Compra {self.data:%d/%m/%Y} no valor total R$ {self.total}. Cliente {self.cliente.nome}.'


auditlog.register(Compra)


class DetalheCompra(TimeStampedModel):

    compra = models.ForeignKey(Compra, related_name='detalhe_compra', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, related_name='detalhe_compra', on_delete=models.CASCADE)

    total = models.DecimalField(max_digits=9, decimal_places=2)
    quantidade = models.IntegerField()

    def __str__(self):
        return f'{self.compra} Produto={self.produto}, total={self.total}, quantidade={self.quantidade}'


auditlog.register(DetalheCompra)
