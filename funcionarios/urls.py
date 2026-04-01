from django.urls import path
from . import views

urlpatterns = [
    path('', views.funcionarios, name='funcionarios'),
    path('adicionar/', views.adicionar_funcionario, name='adicionar_funcionario'),
    path('editar/<int:id>/', views.editar_funcionario, name='editar_funcionario'),
    path('excluir/<int:id>/', views.excluir_funcionario, name='excluir_funcionario'),
]