from django.urls import path
from usuarios.views import login, cadastro, index
urlpatterns = [
    path('cadastro', cadastro, name = 'cadastro'),
    path('login', login, name = 'login'),
    path('', index, name='index')

]