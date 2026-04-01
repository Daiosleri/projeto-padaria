from django.shortcuts import render, get_object_or_404, redirect
from .models import Funcionario
from django import forms


class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'cargo', 'turno', 'salario', 'telefone', 'data_admissao', 'ativo']
        widgets = {
            'data_admissao': forms.DateInput(attrs={'type': 'date'}),
        }


def funcionarios(request):
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