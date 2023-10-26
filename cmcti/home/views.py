from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from home.models import Demanda
from register.models import CustomUser
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from home.thread import SendEmailThread

#consume api
import requests
from django.http import HttpResponse
import json
#from easy_pdf.rendering import render_to_pdf_response
from datetime import datetime

# Create your views here.

@login_required(login_url='/entrar')
def homeView(request):
    
    response = requests.get('http://127.0.0.1:8080/items/')
    
    #convert reponse data into json
    api_data = response.json()
    data_list = []
    for objs in api_data:
        data_list.append(objs)
        
    

    if request.method == 'POST':
        user = CustomUser.objects.get(email=request.user.email)
        data = None
        titulo = str(request.POST['titulo'])
        descricao = str(request.POST['descricao'])
        tipo = str(request.POST['tipo'])
        file = request.FILES['doc'] or None

        if request.POST['data']:
            data = str(request.POST['data'])

        if file:
            demanda = Demanda.objects.create(titulo=titulo, tipo=tipo, descricao=descricao, prazo=data, documento=file)
            demanda.criado_por.add(user)
            SendEmailThread(titulo).start()
        else:
            demanda = Demanda.objects.create(titulo=titulo, tipo=tipo, descricao=descricao, prazo=data)
            demanda.criado_por.add(user)
            SendEmailThread(titulo).start()
        

        
        

        messages.add_message(request, messages.SUCCESS, f"{tipo} cadastrada(o) com sucesso!")
    return render(request, 'pages/home.html', {'products': data_list})


@login_required(login_url='/entrar')
def demandasView(request):

    demandas = Demanda.objects.all()


    return render(request, 'pages/verDemandas.html', {'demandas':demandas})

@login_required(login_url='/entrar')
def documentosView(request):

    demandas = Demanda.objects.all()


    return render(request, 'pages/verDocumentos.html', {'demandas':demandas})

@login_required(login_url='/entrar')
def demandaConcluida(request, id):

    demanda = Demanda.objects.get(pk=id)

    demanda.concluida = True
    demanda.save()

    messages.add_message(request, messages.SUCCESS, "Demanda marcada como conluída!")
    return HttpResponseRedirect('/demandas')


def deletarDemanda(request, tipo, id):

    demanda = Demanda.objects.get(pk=id)
    demanda.delete()

    messages.add_message(request, messages.SUCCESS, "Demanda deletada com sucesso!")

    if str(tipo) == 'Demanda':
        return redirect('/demandas')
    
    if str(tipo) == 'Documento':
        return redirect('/documentos')
        

@staff_member_required(login_url="/")
@login_required(login_url='/entrar')
def usuariosView(request):

    usuarios = CustomUser.objects.all()

    return render(request, 'pages/usuarios.html', {'usuarios':usuarios})

@staff_member_required(login_url="/")
@login_required(login_url='/entrar')
def usuariosUpgradeView(request, id):
    usuario = CustomUser.objects.get(id=id)
    if usuario.is_staff == False:
        usuario.is_staff = True
        usuario.save()
        messages.add_message(request, messages.SUCCESS, "Usuário promovido a diretoria")
        return redirect('/diretoria/usuarios')
    else:
        messages.add_message(request, messages.ERROR, "Usuário ja pertence à diretoria")
        return redirect('/diretoria/usuarios')

@staff_member_required(login_url="/")
@login_required(login_url='/entrar')
def usuariosDowngradeView(request, id):
    usuario = CustomUser.objects.get(id=id)
    if usuario.is_staff == True:
        usuario.is_staff = False
        usuario.save()
        messages.add_message(request, messages.SUCCESS, "Cargo de diretoria desatribuído ao usuário")
        return redirect('/diretoria/usuarios')
    else:
        messages.add_message(request, messages.ERROR, "Usuário não pertence à diretoria")
        return redirect('/diretoria/usuarios')
    

@staff_member_required(login_url="/")
@login_required(login_url='/entrar')
def relatorioView(request):
    demandas = Demanda.objects.all()
    usuarios = CustomUser.objects.all()
    data = datetime.today().strftime("%d/%m/%Y")

    return render_to_pdf_response(request, 'pages/relatorio.html', {'demandas':demandas, 
    'usuarios':usuarios, 'data':data})
    