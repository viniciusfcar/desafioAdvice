from django.urls import path
from .views import cadastro_proprietario, delete_proprietario
from .views import lista_proprietarios
from .views import delete_proprietario
from .views import alterar_proprietario

urlpatterns = [
    path('cadastro_proprietario/', cadastro_proprietario, name='cadastroProprietario'),
    path('lista_proprietarios/', lista_proprietarios, name='listaProprietarios'),
    path('delete_proprietario/<id>/', delete_proprietario, name='deleteProprietario'),
    path('alterar_proprietario/<id>/', alterar_proprietario, name='alterarProprietario'),
]