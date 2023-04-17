from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def homeView(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        descricao = request.POST['descricao']
        data = request.POST['data']

        print(titulo, descricao, data)
    return render(request, 'pages/home.html')
