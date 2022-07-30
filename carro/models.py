from django.db import models
from proprietario.models import Proprietario

class Carro(models.Model):

    COR_CHOICE = (
        ("Amarelo", "AMARELO"),
        ("Azul", "AZUL"),
        ("Cinza", "CINZA")
    )

    MODELO_CHOICE = (
        ("Escotilha", "ESCOTILHA"),
        ("Sedan", "SEDAN"),
        ("Conversível", "CONVERSÍVEL")
    )
    
    cor = models.CharField(max_length=20, choices=COR_CHOICE, blank=True, null=False)
    modelo = models.CharField(max_length=20, choices=MODELO_CHOICE, blank=True, null=False)
    proprietario = models.ForeignKey(Proprietario, on_delete=models.CASCADE, related_name='carros')

    def __str__(self):
        return self.cor + " " + self.modelo
