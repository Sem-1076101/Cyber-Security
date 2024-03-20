from django.shortcuts import render, redirect
from administrators.models import Medewerker, Ervaringsdeskundige, Beperking
from experiential_experts.forms import CreateExpertForm, LoginFormExpert
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError
from companies.models import Onderzoek
from django.shortcuts import get_object_or_404

# Authenticatie imports voor de login
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password

def signup(request):
    if request.method == 'POST':
        form = CreateExpertForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            print(email)
            if Ervaringsdeskundige.objects.filter(email=email).exists():
                messages.success(request, 'E-mail is al in gebruik!')
            else:
                voornaam = request.POST.get('firstName')
                achternaam = request.POST.get('lastName')
                wachtwoord = request.POST.get('password')
                geslacht = request.POST.get('gender')
                telefoonnummer = request.POST.get('phonenumber')
                geboortedatum = request.POST.get('birthday')
                postcode = request.POST.get('zipCode')
                huisnummer = request.POST.get('housenumber')
                soort_beperking = request.POST.get('disability')
                hulpmiddelen = request.POST.get('tools')
                bijzonderheden = request.POST.get('particulars')

                naam_toezichthouder = request.POST.get('supervisorName')
                email_toezichthouder = request.POST.get('email_supervisor')
                telefoonnummer_toezichthouder = request.POST.get('phonenumber_supervisor')
                benadering_keuze = request.POST.get('approach_choice')

                if not naam_toezichthouder or not email_toezichthouder or not telefoonnummer_toezichthouder:
                    naam_toezichthouder = None
                    email_toezichthouder = None
                    telefoonnummer_toezichthouder = None
                
                aanmaken_ervaringsdeskundige = Ervaringsdeskundige.objects.create(
                    voornaam=voornaam,
                    achternaam=achternaam,
                    wachtwoord=wachtwoord,
                    geboortedatum=geboortedatum,
                    telefoonnummer=telefoonnummer,
                    email=email,
                    geslacht=geslacht,
                    postcode=postcode,
                    huisnummer=huisnummer,
                    soort_beperking=soort_beperking,
                    hulpmiddelen=hulpmiddelen,
                    bijzonderheden=bijzonderheden,

                    naam_toezichthouder=naam_toezichthouder,
                    email_toezichthouder=email_toezichthouder,
                    telefoonnummer_toezichthouder=telefoonnummer_toezichthouder,
                    benadering_keuze=benadering_keuze
                )
                if aanmaken_ervaringsdeskundige:
                    return redirect('../login') 
                else:
                    messages.success(request, ('Er is iets fout gegaan, probeer het opnieuw.'))
        else:
            messages.success(request, ('Er is iets fout gegaan, probeer het opnieuw'))
    else:
        form = CreateExpertForm()
    return render(request, 'signupExpert.html', {})          
        


def login(request):
    form = LoginFormExpert()
    if request.method == 'POST':
        form = LoginFormExpert(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            wachtwoord = request.POST.get('wachtwoord')
            print(email, wachtwoord)
            ervaringsdeskundige = Ervaringsdeskundige.objects.filter(email=email).first()
            if ervaringsdeskundige.account_status == 1:
                if ervaringsdeskundige and check_password(wachtwoord, ervaringsdeskundige.wachtwoord):
                    request.session['deskundige_id'] = ervaringsdeskundige.deskundige_id
                    request.session['voornaam'] = ervaringsdeskundige.voornaam
                    request.session['achternaam'] = ervaringsdeskundige.achternaam
                    request.session['email'] = ervaringsdeskundige.email
                    return redirect('../onderzoek-overzicht')
                else:
                    messages.success(request, ('Inloggen mislukt. Ongeldige email of wachtwoord.'))
            else:
                messages.success(request, ('Inloggen mislukt. U moet nog wachten op goedkeuring van uw account!'))
        else:
            messages.success(request, ('Er is iets fout gegaan, probeer het opnieuw.'))
            print('Formulier is niet geldig')
    else:
        print('Geen POST-verzoek ontvangen.')

    context = {'loginform': form}

    return render(request, 'loginExpert.html', context=context)

def home(request):
    return render(request, 'homepageExperts.html', {})

def onderzoek_overzicht(request):
    onderzoeken = Onderzoek.objects.all()

    doelgroep_filter = request.GET.get('doelgroep')
    if doelgroep_filter:
        onderzoeken = onderzoeken.filter(doelgroep_beperking=doelgroep_filter)

    return render(request, 'onderzoek_overzicht.html', {'onderzoeken': onderzoeken})

def inschrijven(request, onderzoek_id, deskundige_id):
    onderzoek = get_object_or_404(Onderzoek, onderzoek_id=onderzoek_id)
    deskundige_id = request.session.get('deskundige_id')

    if deskundige_id:
        ervaringsdeskundige = Ervaringsdeskundige.objects.filter(deskundige_id=request.session['deskundige_id']).first()
        if ervaringsdeskundige:
            ervaringsdeskundige.onderzoek = onderzoek
            ervaringsdeskundige.save()
    
    return redirect('signUpExpert.html')


def uitschrijven(request, onderzoek_id):
    onderzoek = get_object_or_404(Onderzoek, onderzoek_id=onderzoek_id)
    onderzoek.deskundige_id = None
    onderzoek.save()

    return redirect('onderzoek_overzicht')