from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import Cliente
from django.contrib.auth import login
from django.http import HttpResponseRedirect

class Cadastrar(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'cadastrar.html')
    
    def post(self, *args, **kwargs):
      try:
        usuario_aux = User.objects.get(email=self.request.POST['email'])

        if usuario_aux:
            return render(self.request, 'cadastrar.html', {'msg': 'Já existe um usuário com o mesmo e-mail'})
          
      except User.DoesNotExist:        
        usuario = self.request.POST['usuario']
        nome = self.request.POST['nome']
        telefone = self.request.POST['telefone']
        email = self.request.POST['email']
        senha = self.request.POST['senha']
        
        novoUsuario = User.objects.create_user(username=usuario, email=email, password=senha, first_name=nome)
        novoUsuario.save()
        
        cliente = Cliente()
        cliente.user = novoUsuario
        cliente.telefone = telefone
        cliente.save()
        
        login(self.request, novoUsuario)
        return HttpResponseRedirect('/')
        