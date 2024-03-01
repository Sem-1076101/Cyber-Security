from django.shortcuts import render, redirect
from administrators.models import Onderzoek, Medewerker, Organisatie, Ervaringsdeskundige, Beperking
from experiential_experts.forms import CreateExpertForm, LoginFormExpert
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError

# Authenticatie imports voor de login
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password

def signup(request):
    if request.method == 'POST':
        form = CreateExpertForm(request.POST)
        if form.is_valid():
            gebruikersnaam = request.POST.get('gebruikersnaam')
            emailadres = request.POST.get('email')

            if Ervaringsdeskundige.objects.filter(gebruikersnaam=gebruikersnaam).exists():
                messages.success(request, 'Gebruikersnaam is al in gebruik!')
            elif Ervaringsdeskundige.objects.filter(emailadres=emailadres).exists():
                messages.success(request, 'E-mail is al in gebruik!')
            else:
                voornaam = request.POST.get('firstName')
                achternaam = request.POST.get('lastName')
                wachtwoord = request.POST.get('password')
                geslacht = request.POST.get('gender')
                geboortedatum = request.POST.get('birthday')
                postcode = request.POST.get('zipCode')
                type_beperking = request.POST.get('disability')
                gebruikte_hulpmiddelen = request.POST.get('tools')
                bijzonderheden = request.POST.get('particulars')

                naam_toezichthouder = request.POST.get('supervisorName')
                email_toezichthouder = request.POST.get('email_supervisor')
                telefoonnummer_toezichthouder = request.POST.get('phonenumber_supervisor')
                benadering_keuze = request.POST.get('approach_choice')

                if not naam_toezichthouder or not email_toezichthouder or not telefoonnummer_toezichthouder:
                    naam_toezichthouder = None
                    email_toezichthouder = None
                    telefoonnummer_toezichthouder = None
                
                Ervaringsdeskundige.objects.create(
                    voornaam=voornaam,
                    achternaam=achternaam,
                    geboortedatum=geboortedatum,
                    telefoonnummer=telefoonnummer,
                    email=email,
                    geslacht=geslacht,
                    postcode=postcode,
                    huisnummer=huisnummer,
                    soort_beperking=soort_beperking,
                    hulpmiddelen=hulpmiddelen,
                    bijzonderheden=bijzonderheden,
                )
                # form.save()
                return redirect('../login') 
        else:
            messages.success(request, ('Er is iets fout gegaan, probeer het opnieuw'))
    else:
        form = CreateExpertForm()
    return render(request, 'signupExpert.html', {})          

# def signup(request):
#     if request.method == 'POST':
#         form = CreateExpertForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('../login')
#     else:
#         form = CreateExpertForm()
#     return render(request, 'signupExpert.html', {})          


def login(request):
    form = LoginFormExpert()
    if request.method == 'POST':
        form = LoginFormExpert(request.POST)
        if form.is_valid():
            gebruikersnaam = request.POST.get('gebruikersnaam')
            wachtwoord = request.POST.get('wachtwoord')
            print(gebruikersnaam)
            print(wachtwoord)    
            ervaringsdeskundige = Ervaringsdeskundige.objects.filter(gebruikersnaam=gebruikersnaam).first()
            if ervaringsdeskundige and check_password(wachtwoord, ervaringsdeskundige.wachtwoord):
            # user = authenticate(request, gebruikersnaam=gebruikersnaam, wachtwoord=wachtwoord)
            # if user is not None:
                # login(request, medewerker)
                return redirect('/')
            else:
                messages.success(request, ('Inloggen mislukt. Ongeldige gebruikersnaam of wachtwoord.'))
        else:
            messages.success(request, ('Er is iets fout gegaan, probeer het opnieuw.'))
            print('Formulier is niet geldig')
    else:
        print('Geen POST-verzoek ontvangen.')

    context = {'loginform': form}

    return render(request, 'loginExpert.html', context=context)