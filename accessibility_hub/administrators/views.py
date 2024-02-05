from django.shortcuts import render
from .models import Onderzoek, Medewerker, Organisatie, Ervaringsdeskundige, Beperking


def login(request):
    return render(request, 'login.html', {})


def signup(request):
    return render(request, 'signup.html', {})


def portal(request):
    onderzoeken = Onderzoek.objects.all()[:5]
    medewerkers = Medewerker.objects.all()
    organisaties = Organisatie.objects.all()
    ervaringsdeskundigen = Ervaringsdeskundige.objects.all()
    beperkingen = Beperking.objects.all()
    return render(request, 'portal.html', {'onderzoeken': onderzoeken, 'medewerkers': medewerkers,
                                              'organisaties': organisaties, 'ervaringsdeskundigen': ervaringsdeskundigen, 'beperkingen': beperkingen})
