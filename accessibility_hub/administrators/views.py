from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse
# from .models import Onderzoek, Medewerker, Organisatie, Ervaringsdeskundige, Beperking
from .models import Medewerker, Ervaringsdeskundige, Beperking


def login(request):
    return render(request, 'login.html', {})


def signup(request):
    return render(request, 'signup.html', {})


def portal(request):
    # onderzoeken = Onderzoek.objects.all()[:5]
    medewerkers = Medewerker.objects.all()
    # organisaties = Organisatie.objects.all()
    ervaringsdeskundigen = Ervaringsdeskundige.objects.all()
    beperkingen = Beperking.objects.all()
    # return render(request, 'portal.html', {'onderzoeken': onderzoeken, 'medewerkers': medewerkers,
    #                                           'organisaties': organisaties, 'ervaringsdeskundigen': ervaringsdeskundigen, 'beperkingen': beperkingen})
    return render(request, 'portal.html', {'medewerkers': medewerkers, 'ervaringsdeskundigen': ervaringsdeskundigen, 'beperkingen': beperkingen})

def medewerker(request, medewerker_id):
    medewerker = Medewerker.objects.get(medewerker_id=medewerker_id)
    return render(request, 'employee.html', {'medewerker': medewerker})

def verwijder_medewerker(request, medewerker_id):
    medewerker = get_object_or_404(Medewerker, medewerker_id=medewerker_id)
    medewerker.delete()
    return redirect('administrators:medewerkersportal')
