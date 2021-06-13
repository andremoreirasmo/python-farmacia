# Generated by Django 3.2.4 on 2021-06-13 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('remedio', '0001_initial'),
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('valor', models.FloatField()),
                ('status', models.CharField(default='P', help_text='P - Pendente, C - Cancelado - F - Finalizado', max_length=1)),
                ('endereco', models.TextField(max_length=200)),
                ('receita', models.ImageField(upload_to='media')),
                ('cliente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente')),
                ('remedio', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='remedio.remedio')),
            ],
        ),
    ]