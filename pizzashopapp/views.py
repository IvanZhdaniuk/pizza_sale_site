from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return redirect(pizzashop_home)

@login_required(login_url='pizzashopapp-sing-in')
def pizzashop_home(request):
    return render(request, 'pizzashopapp/home.html', {})

def pizzashopapp_sing_up(requst):
    return render(requst, 'pizzashopapp/sing-up.html', {})
