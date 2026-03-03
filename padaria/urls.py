from django.contrib import admin
from django.urls import path, include
from produtos import views

admin.site.site_header = 'Padaria - Dois Irmãos'
admin.site.site_title = 'Padaria'
admin.site.index_title = 'Bem-vindo ao Sistema da Padaria, dois irmãos'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('produtos/', include('produtos.urls')),
]