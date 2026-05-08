from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Pedido, ItemPedido
from produtos.models import Produto


@login_required
def lista_pedidos(request):
    if request.user.is_staff:
        pedidos = Pedido.objects.all()
    else:
        pedidos = Pedido.objects.filter(funcionario=request.user)

    status = request.GET.get('status')
    if status:
        pedidos = pedidos.filter(status=status)

    return render(request, 'pedidos/lista_pedidos.html', {
        'pedidos': pedidos,
        'status_selecionado': status,
    })


@login_required
def novo_pedido(request):
    pedido = Pedido.objects.create(
        funcionario=request.user,
        forma_pagamento='dinheiro'
    )
    return redirect(f'/pedidos/{pedido.id}/')


@login_required
def detalhe_pedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    produtos = Produto.objects.filter(disponivel=True)

    if request.method == 'POST':
        acao = request.POST.get('acao')

        if acao == 'item':
            produto_id = request.POST.get('produto')
            quantidade = request.POST.get('quantidade')
            produto = get_object_or_404(Produto, id=produto_id)

            item, created = ItemPedido.objects.get_or_create(
                pedido=pedido,
                produto=produto,
                defaults={
                    'quantidade': quantidade,
                    'preco_unitario': produto.preco
                }
            )
            if not created:
                item.quantidade = float(item.quantidade) + float(quantidade)
                item.save()

            pedido.calcular_total()

        elif acao == 'observacao':
            pedido.observacao = request.POST.get('observacao', '')
            pedido.save()

        return redirect(f'/pedidos/{id}/')

    return render(request, 'pedidos/detalhe_pedido.html', {
        'pedido': pedido,
        'produtos': produtos,
    })


@login_required
def remover_item(request, id):
    item = get_object_or_404(ItemPedido, id=id)
    pedido_id = item.pedido.id
    pedido = item.pedido
    item.delete()
    pedido.calcular_total()
    return redirect(f'/pedidos/{pedido_id}/')


@login_required
def fechar_pedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    if request.method == 'POST':
        pedido.status = 'fechado'
        forma = request.POST.get('forma_pagamento')
        if forma:
            pedido.forma_pagamento = forma
        pedido.save()
        return redirect('/pedidos/')
    return render(request, 'pedidos/fechar_pedido.html', {'pedido': pedido})


@login_required
def excluir_pedido(request, id):
    if not request.user.is_staff:
        return redirect('/pedidos/')
    pedido = get_object_or_404(Pedido, id=id)
    if request.method == 'POST':
        pedido.delete()
        return redirect('/pedidos/')
    return render(request, 'pedidos/excluir_pedido.html', {'pedido': pedido})