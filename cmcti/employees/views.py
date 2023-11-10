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

    response = requests.get('http://127.0.0.1:8080/users/')

    print(response)
    user = requests.get(f'http://127.0.0.1:8080/users/{request.user}')

    user_data = user.json()
    user_id = user_data['id']
    
    #convert reponse data into json
    api_data = response.json()
    data_list = []
    for objs in api_data:
        data_list.append(objs)
    
    print(data_list)
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
            'price': value,
            'owner': add_by
        }

        new_request = requests.post(f'http://127.0.0.1:8080/users/{user_id}/items', json=json_data)
        messages.add_message(request, messages.SUCCESS, "Registro adicionado com sucesso!")
        return redirect('/painel-admin')
    return render(request, 'pages/adminPanel.html', context)