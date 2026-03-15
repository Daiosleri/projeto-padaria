from django.shortcuts import render

def funcionarios(request):
    return render(request, 'funcionarios/funcionarios.html')