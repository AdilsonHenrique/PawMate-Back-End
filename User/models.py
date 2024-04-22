from django.db import models
from django.contrib.auth.models import User

class PerfilPawmate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome_dono = models.CharField(max_length=100)
    cidade_dono = models.CharField(max_length=100)
    estado_dono = models.CharField(max_length=100)
    pais_dono = models.CharField(max_length=100)
    telefone_dono = models.CharField(max_length=15)

    nome_animal = models.CharField(max_length=100)
    idade_animal = models.IntegerField()
    raca_animal = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_dono