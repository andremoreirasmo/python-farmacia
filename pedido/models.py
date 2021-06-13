from django.db import models
from remedio.models import Remedio;
from clientes.models import Cliente;

# Create your models here.
class Pedido(models.Model):
    remedio = models.ForeignKey(Remedio, on_delete=models.CASCADE,null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE,null=True)
    quantidade = models.IntegerField(null=False)
    valor = models.FloatField(null=False)
    status = models.CharField(max_length=1, default='P', help_text='P - Pendente, C - Cancelado - F - Finalizado')
    endereco = models.TextField(max_length=200)
    receita = models.ImageField(upload_to='media')
    dataEntraga = models.DateField(null=True)

    def __str__(self):
        return 'Pedido'