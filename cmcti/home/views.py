from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from home.models import Demanda
from django.contrib.auth import get_user_model

# Create your views here.

@login_required(login_url='/entrar')
def homeView(request):
    if request.method == 'POST':
        user_model = get_user_model()
        user = user_model.objects.get(email=request.user.email)
        data = ""
        titulo = str(request.POST['titulo'])
        descricao = str(request.POST['descricao'])
        if request.POST['data']:
            data = str(request.POST['data'])

        Demanda.objects.create(titulo=titulo, descricao=descricao, prazo=data, criado_por=user)

    return render(request, 'pages/home.html')

@login_required(login_url='/entrar')
def demandasView(request):

    demandas = Demanda.objects.all()

    return render(request, 'pages/verDemandas.html', {'demandas':demandas})