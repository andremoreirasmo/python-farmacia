"""meuProjeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from django.urls import include
from clientes.views import *
from remedio.views import *
from pedido.views import *


#so temos a pagina admin por hora

urlpatterns = [
    path('', home),
    path('pedidos/', pedidos),
    path('comprar/<int:id>', comprarRemedio),  
    path('efetivarPedido', efetivarPedido),
    path('areaRestrita/', areaRestrita),
    path('areaRestrita/remedio/', cadastrarRemedio),
    path('areaRestrita/remedio/alterar/<int:id>', editarRemedio),  
    path('areaRestrita/remedio/alterar/salvar/<int:id>', alterarRemedio),  
    path('areaRestrita/remedio/excluir/<int:id>', deletarRemedio),
    path('areaRestrita/alterarPedido/<int:id>', alterarPedido),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls'), name='accounts'),
    path('cadastrar/', Cadastrar.as_view(), name='cadastrar')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
