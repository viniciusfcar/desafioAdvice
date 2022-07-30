from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.test.client import Client

class AccountsViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        User.objects.create_user('admin', 'admin@gmail.com', '123')

    def test_login_requerid(self):
        response = self.client.post('/', {'username': 'admin', 'password': '123'})
        self.assertRedirects(response, '/index/')

    def test_logout_requerid(self):
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, '/')