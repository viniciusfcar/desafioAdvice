from django.test import TestCase
from ..models import Carro
from proprietario.models import Proprietario

class CarroModelTestCase(TestCase):

    def setUp(self):
        prop = Proprietario.objects.create(nome='Carneiro', potencialComprador='False', totalCarros=1)
        Carro.objects.create(cor='Azul', modelo='Escotilha', proprietario=prop)

    def test_criacao_carro(self):
        prop = Proprietario.objects.create(nome='Vinicius', potencialComprador='True', totalCarros=0)
        carro = Carro.objects.create(cor='Amarelo', modelo='Sedan', proprietario=prop)

        self.assertTrue(carro)

    def test_return_str(self):
        carro = Carro.objects.get(cor='Azul', modelo='Escotilha')

        self.assertEquals(carro.__str__(), 'Azul Escotilha')
