from django.contrib import admin
from .models import Categoria, Produto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    search_fields = ('nome',)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'tipo_preco', 'preco_formatado', 'disponivel')
    search_fields = ('nome',)
    list_filter = ('categoria', 'tipo_preco', 'disponivel')