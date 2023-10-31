from django.urls import path
from employees import views

urlpatterns = [
    path('painel-admin', views.painelAdmin, name="painelAdmin")
]