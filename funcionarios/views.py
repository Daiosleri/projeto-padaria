from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Funcionario
from django import forms


class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['usuario', 'nome', 'cargo', 'turno', 'salario', 'telefone', 'data_admissao', 'ativo']
        widgets = {
            'data_admissao': forms.DateInput(attrs={'type': 'date'}),
        }


@login_required
def funcionarios(request):
    if not request.user.is_staff:
        return redirect('/')

    lista = Funcionario.objects.all()
    cargo = request.GET.get('cargo')
    turno = request.GET.get('turno')

    if cargo:
        lista = lista.filter(cargo=cargo)
    if turno:
        lista = lista.filter(turno=turno)

    total_ativos = Funcionario.objects.filter(ativo=True).count()

    return render(request, 'funcionarios/funcionarios.html', {
        'funcionarios': lista,
        'total_ativos': total_ativos,
        'cargo_selecionado': cargo,
        'turno_selecionado': turno,
    })


@login_required
def adicionar_funcionario(request):
    if not request.user.is_staff:
        return redirect('/')
    form = FuncionarioForm()
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/funcionarios/')
    return render(request, 'funcionarios/form_funcionario.html', {'form': form})


@login_required
def editar_funcionario(request, id):
    if not request.user.is_staff:
        return redirect('/')
    funcionario = get_object_or_404(Funcionario, id=id)
    form = FuncionarioForm(instance=funcionario)
    if request.method == 'POST':
        form = FuncionarioForm(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            return redirect('/funcionarios/')
    return render(request, 'funcionarios/form_funcionario.html', {'form': form})


@login_required
def excluir_funcionario(request, id):
    if not request.user.is_staff:
        return redirect('/')
    funcionario = get_object_or_404(Funcionario, id=id)
    if request.method == 'POST':
        funcionario.delete()
        return redirect('/funcionarios/')
    return render(request, 'funcionarios/excluir_funcionario.html', {'funcionario': funcionario})