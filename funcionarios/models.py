from django.db import models

class Funcionario(models.Model):
    CARGO_CHOICES = [
        ('gerente', 'Gerente'),
        ('caixa', 'Caixa'),
        ('atendente', 'Atendente'),
        ('padeiro', 'Padeiro'),
    ]

    TURNO_CHOICES = [
        ('manha', 'Manha'),
        ('tarde', 'Tarde'),
        ('noite', 'Noite'),
    ]

    nome = models.CharField(max_length=200)
    cargo = models.CharField(max_length=20, choices=CARGO_CHOICES)
    turno = models.CharField(max_length=10, choices=TURNO_CHOICES)
    salario = models.DecimalField(max_digits=8, decimal_places=2)
    telefone = models.CharField(max_length=20, blank=True)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'