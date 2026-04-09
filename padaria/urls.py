from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from produtos import views

admin.site.site_header = 'Padaria - Dois Irmaos'
admin.site.site_title = 'Padaria'
admin.site.index_title = 'Bem-vindo ao Sistema da Padaria, dois irmaos'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', include('autenticacao.urls')),
    path('produtos/', include('produtos.urls')),
    path('funcionarios/', include('funcionarios.urls')),
    path('pedidos/', include('pedidos.urls')),
    path('relatorios/', include('relatorios.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)