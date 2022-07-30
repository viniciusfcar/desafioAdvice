from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.test.client import Client

class PessoaViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        User.objects.create_user('admin', 'admin@gmail.com', '123')
    
    def test_lista_proprietarios_retorn_status_200(self):
        self.client.login(username='admin', password='123')
        response = self.client.get(reverse("listaProprietarios"))
        self.assertEqual(response.status_code, 200)