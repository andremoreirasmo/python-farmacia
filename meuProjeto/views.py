from django.http import HttpResponse
from django.shortcuts import render
from remedio.models import Remedio
from clientes.models import Cliente
from pedido.models import Pedido
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect


def home(request):
    remedios = Remedio.objects.all()
    return render(request, 'index.html', {'remedios': remedios})


@user_passes_test(lambda u: u.is_staff, login_url='/accounts/login/')
def areaRestrita(request):
    remedios = Remedio.objects.all()
    pedidos = Pedido.objects.all()
    clientes = Cliente.objects.all()
    return render(request, 'areaRestrita.html', {'remedios': remedios, 'pedidos': pedidos, 'clientes': clientes})


@user_passes_test(lambda u: u.is_authenticated, login_url='/accounts/login/')
def pedidos(request):
    pedidos = Pedido.objects.filter(cliente__user__id=request.user.id)
    return render(request, 'pedidos.html', {'pedidos': pedidos})


@user_passes_test(lambda u: u.is_authenticated, login_url='/accounts/login/')
def comprarRemedio(request, id):
    remedio = Remedio.objects.get(id=id)
    return render(request, 'comprar_remedio.html', {'remedio': remedio})


@user_passes_test(lambda u: u.is_authenticated, login_url='/accounts/login/')
def alterarPedido(request, id):
    pedido = Pedido.objects.get(id=id)

    if request.method == 'POST':
        remedio = Remedio.objects.get(id=pedido.remedio.id)

        pedido.quantidade = int(request.POST['quantidade'])
        pedido.endereco = request.POST['endereco']
        pedido.valor = remedio.valor * pedido.quantidade
        pedido.status = request.POST['status']

        pedido.save()

        return HttpResponseRedirect('/areaRestrita')
    else:
        pedido = Pedido.objects.get(id=id)
        return render(request, 'alterar_pedido.html', {'pedido': pedido})

