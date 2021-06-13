from django.db import models

# Create your models here.
class Remedio(models.Model):
    nome = models.CharField(max_length=100, unique=True, help_text='Nome')
    valor = models.FloatField(null=False, help_text='Valor')
    detalhe = models.CharField(max_length=500, null=True)
    foto = models.ImageField(upload_to='media')

    def __str__(self):
        return self.nome