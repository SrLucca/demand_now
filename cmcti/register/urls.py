from django.urls import path
from register import views

urlpatterns = [
    path('entrar', views.loginView, name="entrar"),
    path('sair', views.logoutView, name="logout")
]