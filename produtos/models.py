from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Produto(models.Model):
    TIPO_PRECO_CHOICES = [
        ('unidade', 'Por Unidade'),
        ('kg', 'Por Kg'),
    ]
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    tipo_preco = models.CharField(
        max_length=10,
        choices=TIPO_PRECO_CHOICES,
        default='unidade',
        verbose_name='Tipo de Preco'
    )
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    disponivel = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    def preco_formatado(self):
        if self.tipo_preco == 'kg':
            return f'R$ {self.preco:.2f}/kg'.replace('.', ',')
        return f'R$ {self.preco:.2f}/un'.replace('.', ',')

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'