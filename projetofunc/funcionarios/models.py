from django.db import models

# Create your models here.

class Funcionario(models.Model):
    apelido = models.CharField(max_length=32)
    nome_Completo = models.CharField(max_length=100)
    data_Nasc = models.DateField()
    stacks = models.TextField(blank=True)


