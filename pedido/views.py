from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.files.storage import default_storage
from .models import Pedido
from remedio.models import Remedio
from clientes.models import Cliente
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.


def efetivarPedido(request):
    remedioId = request.POST['remedio']
    quantidade = int(request.POST['quantidade'])
    endereco = request.POST['endereco']
    
    try:
      receita = request.FILES['receita']
      receita_nome = default_storage.save('media/' + receita.name, receita)
    except MultiValueDictKeyError:
      receita_nome = ''
          
    remedio = Remedio.objects.get(id=remedioId) 
    cliente = Cliente.objects.get(user__id=request.user.id) 
    
    pedido = Pedido()
    pedido.remedio = remedio
    pedido.cliente = cliente
    pedido.quantidade = quantidade
    pedido.valor = remedio.valor * quantidade 
    pedido.status = 'P'
    pedido.endereco = endereco
    pedido.receita = receita_nome
    pedido.save()

    return HttpResponseRedirect('/pedidos')
