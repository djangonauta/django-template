from django.contrib import admin

from . import models


@admin.register(models.Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Produto)
class ProdutoAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Cliente)
class ClienteAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Compra)
class CompraAdmin(admin.ModelAdmin):
    pass


@admin.register(models.DetalheCompra)
class DetalheCompraAdmin(admin.ModelAdmin):
    pass
