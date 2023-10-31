from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
@staff_member_required(login_url='/')
@login_required(login_url='/entrar')
def painelAdmin(request):
    
    return render(request, 'pages/adminPanel.html')