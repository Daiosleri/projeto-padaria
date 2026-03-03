from django.contrib import admin
from .models import Categoria, Produto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    search_fields = ('nome',)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'preco_em_reais', 'disponivel')
    search_fields = ('nome',)
    list_filter = ('categoria', 'disponivel')

    def preco_em_reais(self, obj):
        return f'R$ {obj.preco:.2f}'.replace('.', ',')
    preco_em_reais.short_description = 'Preço'