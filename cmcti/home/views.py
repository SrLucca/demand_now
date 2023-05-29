from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from home.models import Demanda
from register.models import CustomUser
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

@login_required(login_url='/entrar')
def homeView(request):
    if request.method == 'POST':
        user = CustomUser.objects.get(email=request.user.email)
        data = ""
        titulo = str(request.POST['titulo'])
        descricao = str(request.POST['descricao'])
        tipo = str(request.POST['tipo'])
        file = request.POST or None

        if request.POST['data']:
            data = str(request.POST['data'])

        if request.POST['doc']:
            file = request.POST['doc']
        

        demanda = Demanda.objects.create(titulo=titulo, tipo=tipo, descricao=descricao, prazo=data, documento=file)
        demanda.criado_por.add(user)

        messages.add_message(request, messages.SUCCESS, f"{tipo} cadastrada(o) com sucesso!")
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

@staff_member_required(login_url="/")
@login_required(login_url='/entrar')
def usuariosView(request):

    usuarios = CustomUser.objects.all()

    return render(request, 'pages/usuarios.html', {'usuarios':usuarios})