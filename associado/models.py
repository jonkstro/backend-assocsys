from django.db import models


class Associado(models.Model):
    nome = models.CharField(max_length=64, blank=False, null=False)
    email = models.EmailField(max_length=64, blank=False, null=False, unique=True)
    cpf = models.CharField(max_length=20, blank=False, null=False, unique=True)
    matricula = models.CharField(max_length=20, blank=False, null=False, unique=True)
    associacao = models.CharField(max_length=20, blank=False, null=False)
    data_nasc = models.DateField(blank=False, null=False)
    data_exped = models.DateField(blank=False, null=False)
    data_valid = models.DateField(blank=False, null=False)
    foto = models.ImageField(upload_to='carteiras')

    def __str__(self):
        return self.nome
