from django.db import models

from associado.models import Associado


class Carteira(models.Model):
    associado = models.ForeignKey(Associado, on_delete=models.CASCADE)
    carteira = models.ImageField(upload_to="carteiras")

    def __str__(self):
        return self.associado.nome
