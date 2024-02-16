from django.shortcuts import render, redirect
from .models import Onderzoek, Medewerker, Organisatie, Ervaringsdeskundige, Beperking
from .forms import CreateEmployeeForm, LoginForm
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError

# Authenticatie imports voor de login
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout 


               

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('gebruikersnaam')
            password = request.POST.get('wachtwoord')
            # hashed_pw_from_usermodel = Medewerker.objects.all().first().wachtwoord
            print(username)
            print(password)
            user = authenticate(request, gebruikersnaam=username, wachtwoord = password)
            if user is not None:
                login(request, user)
                return redirect('../portal')
                # auth.login(request, userCheck)
            else:
                messages.success(request, ('Inloggen mislukt. Ongeldige gebruikersnaam of wachtwoord.'))
                print('Inloggen mislukt. Ongeldige gebruikersnaam of wachtwoord. komt niet voorbij usercheck')
                # return redirect('../login')
        else:
            print('Formulier is niet geldig')
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
