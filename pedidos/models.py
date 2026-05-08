from django.db import models
from django.contrib.auth.models import User
from produtos.models import Produto


class Pedido(models.Model):
    STATUS_CHOICES = [
        ('aberto', 'Aberto'),
        ('fechado', 'Fechado'),
    ]

    PAGAMENTO_CHOICES = [
        ('dinheiro', 'Dinheiro'),
        ('debito', 'Cartao Debito'),
        ('credito', 'Cartao Credito'),
        ('pix', 'Pix'),
    ]

    funcionario = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Funcionario'
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='aberto')
    forma_pagamento = models.CharField(max_length=10, choices=PAGAMENTO_CHOICES, default='dinheiro')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    observacao = models.TextField(blank=True, null=True, verbose_name='Observacao')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Pedido #{self.id} - {self.get_status_display()}'

    def calcular_total(self):
        total = sum(item.subtotal() for item in self.itens.all())
        self.total = total
        self.save()

    def total_formatado(self):
        return f'R$ {self.total:.2f}'.replace('.', ',')

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['-criado_em']


class ItemPedido(models.Model):
    pedido = models.ForeignKey(
        Pedido,
        on_delete=models.CASCADE,
        related_name='itens'
    )
    produto = models.ForeignKey(
        Produto,
        on_delete=models.CASCADE
    )
    quantidade = models.DecimalField(max_digits=8, decimal_places=3)
    preco_unitario = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.produto.nome} x {self.quantidade}'

    def subtotal(self):
        return self.quantidade * self.preco_unitario

    def subtotal_formatado(self):
        return f'R$ {self.subtotal():.2f}'.replace('.', ',')

    class Meta:
        verbose_name = 'Item do Pedido'
        verbose_name_plural = 'Itens do Pedido'