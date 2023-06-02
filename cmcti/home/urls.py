from django.urls import path
from home import views
urlpatterns = [
    path('', views.homeView, name="home_page"),
    path('demandas', views.demandasView, name="demandas"),
    path('documentos', views.documentosView, name="documentos"),
    path('demanda/<int:id>', views.demandaConcluida, name="demandaConcluida"),
    path('deletar/<str:tipo>/<int:id>', views.deletarDemanda, name="deletar"),
    path('diretoria/usuarios', views.usuariosView, name="usuariospage"),
]
