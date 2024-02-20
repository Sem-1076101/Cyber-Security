from django.shortcuts import render, redirect
from .models import Onderzoek, Medewerker, Organisatie, Ervaringsdeskundige, Beperking
from .forms import CreateEmployeeForm, LoginForm
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError

# Authenticatie imports voor de login
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password

            # user = authenticate(request, username=gebruikersnaam, password=wachtwoord)
            # if user is not None:
            #     login(request, user)
            #     return redirect('../portal')
            #     # auth.login(request, userCheck)
            # else:
            #     messages.success(request, ('Inloggen mislukt. Ongeldige gebruikersnaam of wachtwoord.'))
            #     print('Inloggen mislukt. Ongeldige gebruikersnaam of wachtwoord. komt niet voorbij usercheck')
            #     # return redirect('../login')

def signup(request):
    if request.method == 'POST':
        form = CreateEmployeeForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('../login')
    else:
        form = CreateEmployeeForm()
    return render(request, 'signup.html', {'form': form})          


def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            gebruikersnaam = request.POST.get('gebruikersnaam')
            wachtwoord = request.POST.get('wachtwoord')
            print(gebruikersnaam)
            print(wachtwoord)    
            medewerker = Medewerker.objects.filter(gebruikersnaam=gebruikersnaam).first()
            if medewerker and check_password(wachtwoord, medewerker.wachtwoord):
            # user = authenticate(request, gebruikersnaam=gebruikersnaam, wachtwoord=wachtwoord)
            # if user is not None:
                # login(request, medewerker)
                return redirect('../portal')
            else:
                messages.success(request, ('Inloggen mislukt. Ongeldige gebruikersnaam of wachtwoord.'))
        else:
            print('Formulier is niet geldig')
    else:
        print('Geen POST-verzoek ontvangen.')

    context = {'loginform': form}

    return render(request, 'login.html', context=context)

def logout_view(request):
    logout(request)
    return redirect('login') 




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
