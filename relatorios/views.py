from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta
from pedidos.models import Pedido, ItemPedido
from django.db.models import Sum, Count
from django.db.models.functions import TruncDay, TruncMonth
import datetime


@login_required
def relatorios(request):
    if not request.user.is_staff:
        return redirect('/')

    periodo = request.GET.get('periodo', '7dias')
    mes_especifico = request.GET.get('mes', '')
    hoje = timezone.localdate()

    if periodo == '7dias':
        inicio = hoje - timedelta(days=7)
        vendas = (
            Pedido.objects.filter(status='fechado', criado_em__date__gte=inicio)
            .annotate(periodo=TruncDay('criado_em'))
            .values('periodo')
            .annotate(total=Sum('total'), quantidade=Count('id'))
            .order_by('periodo')
        )
        label_periodo = 'Ultimos 7 dias'

    elif periodo == '30dias':
        inicio = hoje - timedelta(days=30)
        vendas = (
            Pedido.objects.filter(status='fechado', criado_em__date__gte=inicio)
            .annotate(periodo=TruncDay('criado_em'))
            .values('periodo')
            .annotate(total=Sum('total'), quantidade=Count('id'))
            .order_by('periodo')
        )
        label_periodo = 'Ultimo mes'

    elif periodo == 'mes' and mes_especifico:
        try:
            ano, mes = mes_especifico.split('-')
            inicio = datetime.date(int(ano), int(mes), 1)
            if int(mes) == 12:
                fim = datetime.date(int(ano) + 1, 1, 1)
            else:
                fim = datetime.date(int(ano), int(mes) + 1, 1)
            vendas = (
                Pedido.objects.filter(
                    status='fechado',
                    criado_em__date__gte=inicio,
                    criado_em__date__lt=fim
                )
                .annotate(periodo=TruncDay('criado_em'))
                .values('periodo')
                .annotate(total=Sum('total'), quantidade=Count('id'))
                .order_by('periodo')
            )
            label_periodo = f'Mes {mes}/{ano}'
        except:
            inicio = hoje - timedelta(days=30)
            vendas = Pedido.objects.none()
            label_periodo = 'Mes especifico'

    else:
        inicio = hoje - timedelta(days=365)
        vendas = (
            Pedido.objects.filter(status='fechado', criado_em__date__gte=inicio)
            .annotate(periodo=TruncMonth('criado_em'))
            .values('periodo')
            .annotate(total=Sum('total'), quantidade=Count('id'))
            .order_by('periodo')
        )
        label_periodo = 'Ultimos 12 meses'

    total_geral = sum(v['total'] for v in vendas) if vendas else 0
    total_pedidos = sum(v['quantidade'] for v in vendas) if vendas else 0

    labels = [v['periodo'].strftime('%d/%m/%Y') for v in vendas]
    dados_total = [float(v['total']) for v in vendas]
    dados_quantidade = [v['quantidade'] for v in vendas]

    produtos_mais_vendidos = (
        ItemPedido.objects.filter(
            pedido__status='fechado',
            pedido__criado_em__date__gte=inicio
        )
        .values('produto__nome')
        .annotate(
            total_quantidade=Sum('quantidade'),
            total_faturado=Sum('preco_unitario')
        )
        .order_by('-total_quantidade')[:10]
    )

    labels_produtos = [p['produto__nome'] for p in produtos_mais_vendidos]
    dados_produtos = [float(p['total_quantidade']) for p in produtos_mais_vendidos]

    return render(request, 'relatorios/relatorios.html', {
        'vendas': vendas,
        'periodo': periodo,
        'mes_especifico': mes_especifico,
        'label_periodo': label_periodo,
        'total_geral': total_geral,
        'total_pedidos': total_pedidos,
        'labels': labels,
        'dados_total': dados_total,
        'dados_quantidade': dados_quantidade,
        'produtos_mais_vendidos': produtos_mais_vendidos,
        'labels_produtos': labels_produtos,
        'dados_produtos': dados_produtos,
    })