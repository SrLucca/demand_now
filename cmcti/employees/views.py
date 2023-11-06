from django.shortcuts import render
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
        for objs in request:
            print(objs)
    return render(request, 'pages/adminPanel.html', context)