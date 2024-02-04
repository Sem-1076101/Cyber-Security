from django.shortcuts import render
from .models import Onderzoeken, Medewerkers

def login(request):
    return render(request, 'login.html', {})

def signup(request):
    return render(request, 'signup.html', {})

def dashboard(request):
    recente_onderzoeken = Onderzoeken.objects.all()[:5]
    medewerkers = Medewerkers.objects.all()
    return render(request, 'dashboard.html', {'recente_onderzoeken': recente_onderzoeken, 'medewerkers': medewerkers})
