from django.urls import path
from .views import lista_carros
from .views import cadastro_carro
from .views import delete_carro

urlpatterns = [
    path('lista_carros/', lista_carros, name='listaCarros'),
    path('cadastro_carro/<id>/', cadastro_carro, name='cadastroCarro'),
    path('delete_carro/<id>/', delete_carro, name='deleteCarro'),
]