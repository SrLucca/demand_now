from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
import requests
from django.http import HttpResponse
import json

# Create your views here.
@staff_member_required(login_url='/')
@login_required(login_url='/entrar')
def painelAdmin(request):

    response = requests.get('http://127.0.0.1:8080/items/')
    
    #convert reponse data into json
    api_data = response.json()
    data_list = []
    for objs in api_data:
        data_list.append(objs)
    
    context = {
        'products': data_list
    }

    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['desc']
        value = request.POST['value']
        add_by = request.user.first_name

        json_data = {
            'title': title,
            'description': description,
            'value': value,
            'owner': add_by
        }

        new_request = requests.post('http://127.0.0.1:8080/users/1/items', json=json_data)
        messages.add_message(request, messages.SUCCESS, "Registro adicionado com sucesso!")
        return redirect('/painel-admin')
    return render(request, 'pages/adminPanel.html', context)