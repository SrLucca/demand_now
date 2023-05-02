from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from home.models import Demanda
from register.models import CustomUser
from django.contrib import messages

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


    return render(request, 'pages/verDemandas.html', {'demandas':demandas})

@login_required(login_url='/entrar')
def demandaConcluida(request, id):

    demanda = Demanda.objects.get(pk=id)

    demanda.concluida = True
    demanda.save()

    messages.add_message(request, messages.SUCCESS, "Demanda marcada como conluída!")
    return HttpResponseRedirect('/demandas')