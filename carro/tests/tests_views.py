from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.test.client import Client
from ..models import Carro
from proprietario.models import Proprietario

class PessoaViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        User.objects.create_user('admin', 'admin@gmail.com', '123')
        prop = Proprietario.objects.create(nome='Vinicius', potencialComprador=False, totalCarros=2)
        Carro.objects.create(cor='Amarelo', modelo='Escotilha', proprietario=prop)
        Carro.objects.create(cor='Azul', modelo='Sedan', proprietario=prop)
    
    def test_lista_carros_retorn_status_200(self):
        self.client.login(username='admin', password='123')
        response = self.client.get(reverse("listaCarros"))
        self.assertEqual(response.status_code, 200)