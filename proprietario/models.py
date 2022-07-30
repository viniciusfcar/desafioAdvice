from django.db import models

class Proprietario(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=False)
    potencialComprador = models.BooleanField(default=True)
    totalCarros = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nome
