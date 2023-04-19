from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Create your views here.
def loginView(request):
    email = ""
    senha = ""
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']

    user = authenticate(request, email=email, password=senha)
    
    if user is not None:
        login(request, user)
        return redirect('/')

    else:
        print('ero')
    return render(request, 'pages/login.html')