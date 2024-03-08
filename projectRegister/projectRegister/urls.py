from django.urls import path
from appRegister import views

urlpatterns = [
    path('', views.home, name="home"),
    path('usuarios/', views.usuarios, name="listaUsuarios")
]
