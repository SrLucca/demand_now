from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from home.models import Demanda
from register.models import CustomUser

# Create your views here.

@login_required(login_url='/entrar')
def homeView(request):
    if request.method == 'POST':
        user = CustomUser.objects.get(email=request.user.email)
        data = ""
        titulo = str(request.POST['titulo'])
        descricao = str(request.POST['descricao'])
        file = request.POST or None

        if request.POST['data']:
            data = str(request.POST['data'])

        if request.POST['doc']:
            file = request.POST['doc']
        

        demanda = Demanda.objects.create(titulo=titulo, descricao=descricao, prazo=data, documento=file)
        demanda.criado_por.add(user)

    return render(request, 'pages/home.html')


@login_required(login_url='/entrar')
def demandasView(request):

    demandas = Demanda.objects.all()

    for objects in demandas:
        print(objects.concluida)

    return render(request, 'pages/verDemandas.html', {'demandas':demandas})