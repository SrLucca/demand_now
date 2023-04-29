from django.urls import path
from register import views

urlpatterns = [
    path('entrar', views.loginView, name="entrar"),
    path('cadastrar', views.registerView, name="cadastro"),
    path('sair', views.logoutView, name="logout"),
    path('perfil', views.configProfile, name="perfil")
]