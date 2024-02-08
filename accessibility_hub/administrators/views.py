from django.shortcuts import render, redirect
from .models import Onderzoek, Medewerker, Organisatie, Ervaringsdeskundige, Beperking
from .forms import CreateEmployeeForm

def login(request):
    return render(request, 'login.html', {})

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
