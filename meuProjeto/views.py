from django.http import HttpResponse
from django.shortcuts import render
from remedio.models import Remedio
from clientes.models import Cliente
from pedido.models import Pedido
from django.contrib.auth.decorators import user_passes_test


def home(request):
    remedios = Remedio.objects.all()
    return render(request, 'index.html', {'remedios' : remedios})

@user_passes_test(lambda u:u.is_staff, login_url='/accounts/login/')
def areaRestrita(request):
    remedios = Remedio.objects.all()
    pedidos = Pedido.objects.all()
    clientes = Cliente.objects.all()
    return render(request, 'areaRestrita.html', {'remedios' : remedios, 'pedidos': pedidos, 'clientes': clientes})


@user_passes_test(lambda u:u.is_authenticated, login_url='/accounts/login/')
def pedidos(request):    
    pedidos = Pedido.objects.filter(cliente__user__id=request.user.id)
    return render(request, 'pedidos.html', {'pedidos': pedidos})