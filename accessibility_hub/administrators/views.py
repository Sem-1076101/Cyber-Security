from django.shortcuts import render
from .models import Onderzoeken

def login(request):
    return render(request, 'login.html', {})

def signup(request):
    return render(request, 'signup.html', {})

def dashboard(request):
    recente_onderzoeken = Onderzoeken.objects.all()[:5]
    return render(request, 'dashboard.html', {'recente_onderzoeken': recente_onderzoeken})
