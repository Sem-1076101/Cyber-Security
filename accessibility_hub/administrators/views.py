from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.conf import settings
# from .models import Onderzoek, Medewerker, Organisatie, Ervaringsdeskundige, Beperking
from .models import Medewerker, Ervaringsdeskundige, Beperking
from companies.models import Organisatie


def login(request):
    return render(request, 'login.html', {})


def signup(request):
    return render(request, 'signup.html', {})


def portal(request):
    # onderzoeken = Onderzoek.objects.all()[:5]
    medewerkers = Medewerker.objects.all()
    organisaties = Organisatie.objects.all()
    ervaringsdeskundigen = Ervaringsdeskundige.objects.all()
    beperkingen = Beperking.objects.all()
    # return render(request, 'portal.html', {'onderzoeken': onderzoeken, 'medewerkers': medewerkers,
    #                                           'organisaties': organisaties, 'ervaringsdeskundigen': ervaringsdeskundigen, 'beperkingen': beperkingen})
    return render(request, 'portal.html', {'medewerkers': medewerkers, 'organisaties': organisaties,
                                           'ervaringsdeskundigen': ervaringsdeskundigen, 'beperkingen': beperkingen})


def medewerker(request, medewerker_id):
    medewerker = Medewerker.objects.get(medewerker_id=medewerker_id)
    return render(request, 'employee.html', {'medewerker': medewerker})


def verwijder_medewerker(request, medewerker_id):
    medewerker = get_object_or_404(Medewerker, medewerker_id=medewerker_id)
    medewerker.delete()
    return redirect('administrators:medewerkersportal')


def organisatie(request, id):
    organisatie = Organisatie.objects.get(id=id)
    return render(request, 'organisation.html', {'organisatie': organisatie})


def verwijder_organisatie(request, id):
    organisatie = get_object_or_404(Organisatie, id=id)
    organisatie.delete()
    return redirect('administrators:medewerkersportal')


def accepteer_organisatie(request, id):
    organisatie = get_object_or_404(Organisatie, id=id)
    organisatie.status = 'Geaccepteerd'
    organisatie.save()
    return redirect('administrators:medewerkersportal')


from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def mail(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')
        email = request.POST.get('email', '')
        name = request.POST.get('name', '')

        if message and email and name:
            send_mail(
                'Contactformulier',  # title
                'Test',  # message
                settings.EMAIL_HOST_USER,  # from email
                [email, 'bdeknikker04@gmail.com'],  # to email
                fail_silently=False,
            )
            return render(request, 'signup.html')
        else:
            # Als gegevens ontbreken, keer dan terug naar de oorspronkelijke pagina.
            return render(request, 'portal.html')

    # Als het geen POST-verzoek is, keer dan terug naar de oorspronkelijke pagina.
    return render(request, 'portal.html')

