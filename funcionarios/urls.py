from django.urls import path
from . import views

urlpatterns = [
    path('', views.funcionarios, name='funcionarios'),
    path('adicionar/', views.adicionar_funcionario, name='adicionar_funcionario'),
    path('editar/<int:id>/', views.editar_funcionario, name='editar_funcionario'),
    path('excluir/<int:id>/', views.excluir_funcionario, name='excluir_funcionario'),
    path('<int:id>/', views.detalhe_funcionario, name='detalhe_funcionario'),
    path('documento/excluir/<int:id>/', views.excluir_documento, name='excluir_documento'),
]