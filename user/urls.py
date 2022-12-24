from django.contrib import admin
from django.urls import path
from .views import logar_usuario, cadastrar_usuario, index, signout


urlpatterns = [
    path('login/', logar_usuario, name="login"),
    path('register', cadastrar_usuario, name="register"),
    path('signout', signout, name="signout"),
    path('', index, name="index"),
]