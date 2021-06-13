from django.shortcuts import render, redirect
from .forms import RemedioForm
from .models import Remedio
# Create your views here.


def cadastrarRemedio(request):
    form = RemedioForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('/areaRestrita')
    return render(request, 'cadastrar_remedio.html',  {'form': form})


def editarRemedio(request, id):
    form = RemedioForm(request.POST or None, request.FILES)
    remedio = Remedio.objects.get(id=id)
    remedio.valor = '{:.2f}'.format(remedio.valor)
    return render(request, 'alterar_remedio.html', {'remedio': remedio, 'form': form})


def alterarRemedio(request, id):
    remedio = Remedio.objects.get(id=id)
    form = RemedioForm(request.POST, request.FILES, instance=remedio)
    if form.is_valid():
        form.save()
        return redirect("/areaRestrita")
    return render(request, 'alterar_remedio.html', {'remedio': remedio})


def deletarRemedio(request, id):
    remedio = Remedio.objects.get(id=id)
    remedio.delete()
    return redirect("/areaRestrita")
