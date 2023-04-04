from django.shortcuts import render
from django.contrib.auth import authenticate, login


# Create your views here.

def loginView(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        
    return render(request, 'pages/login.html')