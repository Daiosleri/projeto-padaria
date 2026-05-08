from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pedidos, name='lista_pedidos'),
    path('novo/', views.novo_pedido, name='novo_pedido'),
    path('<int:id>/', views.detalhe_pedido, name='detalhe_pedido'),
    path('<int:id>/fechar/', views.fechar_pedido, name='fechar_pedido'),
    path('<int:id>/excluir/', views.excluir_pedido, name='excluir_pedido'),
    path('item/<int:id>/remover/', views.remover_item, name='remover_item'),
]