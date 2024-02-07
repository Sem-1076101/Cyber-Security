from django.shortcuts import render
from .models import Onderzoek, Medewerker, Organisatie, Ervaringsdeskundige, Beperking


def login(request):

    form = CreateEmployeeForm()

    if request.method == 'POST':
        form = CreateEmployeeForm

    return render(request, 'login.html', {})


def signup(request):
    return render(request, 'signup.html', {})

def signup_employee(request):
    return render(request, 'signup_employees.html', {})

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
