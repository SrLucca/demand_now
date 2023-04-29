from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from register.forms import CustomUserCreationForm
from django.contrib import messages
from register.models import CustomUser, Profile

# Create your views here.
def loginView(request):
    email = ""
    senha = ""
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']

    user = authenticate(request, username=email, password=senha)
    
    if user is not None:
        login(request, user)
        return redirect('/')

    else:
        pass
    return render(request, 'pages/login.html')


def registerView(request):

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cadastro realizado com sucesso!.")
            return redirect('/')
        else:
            messages.error(request, "Campos inválidos, preencha novamente.")
    else:
        form = CustomUserCreationForm()

    return render(request, 'pages/register.html', {'form':form})

@login_required(login_url='/entrar')
def logoutView(request): 
    logout(request)
    return HttpResponseRedirect('/entrar')

@login_required(login_url='/entrar')
def configProfile(request):
    user = CustomUser.objects.filter(username=request.user.username)

    return render(request, 'pages/config_profile.html', {'objetos': user})