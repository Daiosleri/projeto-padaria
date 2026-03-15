from django.shortcuts import render

def pedidos(request):
    return render(request, 'pedidos/pedidos.html')