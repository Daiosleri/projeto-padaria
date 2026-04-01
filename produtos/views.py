from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Produto, Categoria
from django import forms


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'tipo_preco', 'categoria', 'disponivel']


@login_required
def home(request):
    return render(request, 'produtos/home.html')


@login_required
def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/lista_produtos.html', {'produtos': produtos})


@login_required
def adicionar_produto(request):
    categorias = Categoria.objects.all()
    form = ProdutoForm()
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/produtos/')
    return render(request, 'produtos/form_produto.html', {
        'form': form,
        'categorias': categorias
    })


@login_required
def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    categorias = Categoria.objects.all()
    form = ProdutoForm(instance=produto)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('/produtos/')
    return render(request, 'produtos/form_produto.html', {
        'form': form,
        'categorias': categorias
    })


@login_required
def excluir_produto(request, id):
    if not request.user.is_staff:
        return redirect('/produtos/')
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        produto.delete()
        return redirect('/produtos/')
    return render(request, 'produtos/excluir_produto.html', {'produto': produto})