from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=50, null=False, help_text='Telefone')

    def __str__(self):
        return self.user.username