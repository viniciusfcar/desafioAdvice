from django.contrib import admin
from django.urls import path, include
from index import urls as index_urls
from proprietario import urls as proprietario_urls
from carro import urls as carro_urls
from accounts import urls as accounts_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', include(index_urls)),
    path('proprietario/', include(proprietario_urls)),
    path('carro/', include(carro_urls)),
    path('', include(accounts_urls)),
]
