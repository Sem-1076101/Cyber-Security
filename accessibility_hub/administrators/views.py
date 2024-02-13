from django.shortcuts import render, redirect
from .models import Onderzoek, Medewerker, Organisatie, Ervaringsdeskundige, Beperking
from .forms import CreateEmployeeForm, LoginForm

# Authenticatie imports voor de login
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout 

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.cleaned_data.get('username')
            password = request.cleaned_data.get('password')

            userCheck = authenticate(request, gebruikersnaam= username, wachtwoord= password)
            if userCheck is not None:
                auth.login(request, userCheck)
                return redirect('../portal')
            else:
                print('Inloggen mislukt. Ongeldige gebruikersnaam of wachtwoord.')
        else:
            print('Formulier is niet geldig. Fouten: ', form.errors)
    else:
        print('Geen POST-verzoek ontvangen.')
            

    context = {'loginform': form}

    return render(request, 'login.html', context=context)

def signup(request):
    if request.method == 'POST':
        form = CreateEmployeeForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('../login')
    else:
        form = CreateEmployeeForm()
    return render(request, 'signup.html', {'form': form})


def portal(request):
    onderzoeken = Onderzoek.objects.all()[:5]
    medewerkers = Medewerker.objects.all()
    organisaties = Organisatie.objects.all()
    ervaringsdeskundigen = Ervaringsdeskundige.objects.all()
    beperkingen = Beperking.objects.all()
    return render(request, 'portal.html', {'onderzoeken': onderzoeken, 'medewerkers': medewerkers,
                                              'organisaties': organisaties, 'ervaringsdeskundigen': ervaringsdeskundigen, 'beperkingen': beperkingen})

def medewerker(request):
    return render(request, 'employee.html', {})
