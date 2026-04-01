from django.shortcuts import render, get_object_or_404, redirect
from .models import Funcionario
from django import forms


class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'cargo', 'turno', 'salario', 'telefone', 'ativo']


def funcionarios(request):
    lista = Funcionario.objects.all()
    return render(request, 'funcionarios/funcionarios.html', {'funcionarios': lista})


def adicionar_funcionario(request):
    form = FuncionarioForm()
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/funcionarios/')
    return render(request, 'funcionarios/form_funcionario.html', {'form': form})


def editar_funcionario(request, id):
    funcionario = get_object_or_404(Funcionario, id=id)
    form = FuncionarioForm(instance=funcionario)
    if request.method == 'POST':
        form = FuncionarioForm(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            return redirect('/funcionarios/')
    return render(request, 'funcionarios/form_funcionario.html', {'form': form})


def excluir_funcionario(request, id):
    funcionario = get_object_or_404(Funcionario, id=id)
    if request.method == 'POST':
        funcionario.delete()
        return redirect('/funcionarios/')
    return render(request, 'funcionarios/excluir_funcionario.html', {'funcionario': funcionario})