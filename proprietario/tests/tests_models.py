from django.test import TestCase
from ..models import Proprietario

class ProprietarioModelTestCase(TestCase):

    def setUp(self):
        Proprietario.objects.create(nome='Carneiro', potencialComprador='True', totalCarros=0)

    def test_return_str(self):
        prop = Proprietario.objects.get(nome='Carneiro')

        self.assertEquals(prop.__str__(), 'Carneiro')
