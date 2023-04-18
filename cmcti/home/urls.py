from django.urls import path
from home import views
urlpatterns = [
    path('', views.homeView, name="home_page"),
    path('demandas', views.demandasView, name="demandas"),
]
