from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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
        print('ero')
    return render(request, 'pages/login.html')

@login_required(login_url='/entrar')
def logoutView(request): 
    logout(request)
    return HttpResponseRedirect('/entrar')