from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from .models import Medewerker, Ervaringsdeskundige, Beperking
from companies.models import Organisatie, Onderzoek


def login(request):
    return render(request, 'login.html', {})


def signup(request):
    return render(request, 'signup.html', {})


def portal(request):
    onderzoeken = Onderzoek.objects.all()
    medewerkers = Medewerker.objects.all()
    organisaties = Organisatie.objects.all()
    ervaringsdeskundigen = Ervaringsdeskundige.objects.all()
    beperkingen = Beperking.objects.all()
    return render(request, 'portal.html',
                  {'onderzoeken': onderzoeken, 'medewerkers': medewerkers, 'organisaties': organisaties,
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
    organisatie.status = 'Afgekeurd'
    organisatie.save()

    message = (
        f'Beste {organisatie.first_name} {organisatie.last_name},\n\n'
        f'Uw aanvraag is afgekeurd. Helaas kunnen wij u geen toegang geven tot de applicatie.\n\n'
        f'Met vriendelijke groet,\n'
        'Het team van de Accessibility Hub'
    )

    send_mail(
        'Afkeuring van uw aanvraag',
        message,
        settings.EMAIL_HOST_USER,
        [organisatie.email],
        fail_silently=False,
    )
    return redirect('administrators:medewerkersportal')


def accepteer_organisatie(request, id):
    organisatie = get_object_or_404(Organisatie, id=id)
    organisatie.status = 'Geaccepteerd'
    organisatie.save()

    message = (
        f'Beste {organisatie.first_name} {organisatie.last_name},\n\n'
        f'Uw aanvraag is geaccepteerd. U kunt nu inloggen op de website.\n'
        f'Hier is uw persoonlijke API-sleutel: {organisatie.token}\n\n'
        f'Met vriendelijke groet,\n'
        'Het team van de Accessibility Hub'
    )

    send_mail(
        'Goedkeuring van uw aanvraag',
        message,
        settings.EMAIL_HOST_USER,
        [organisatie.email],
        fail_silently=False,
    )
    return redirect('administrators:medewerkersportal')


def mail(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')

        if message and email and subject:
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            return redirect('administrators:signup')
        else:
            print("Dat ging mis")
            return render(request, 'mail.html')

    return render(request, 'mail.html')


def check_updates_organisaties(request):
    recent_organisaties = Organisatie.objects.filter(status='Nieuw').order_by('date_joined')[:10]

    data = [{'id': organisatie.id, 'bedrijfsnaam': organisatie.bedrijfsnaam, 'email': organisatie.email,
             'first_name': organisatie.first_name,
             'last_name': organisatie.last_name, 'status': organisatie.status, 'date_joined': organisatie.date_joined}
            for organisatie in
            recent_organisaties]

    return JsonResponse(data, safe=False)


def onderzoek(request, onderzoek_id):
    onderzoek = Onderzoek.objects.get(onderzoek_id=onderzoek_id)
    return render(request, 'research.html', {'onderzoek': onderzoek})


def check_updates_onderzoek(request):
    recent_onderzoeken = Onderzoek.objects.filter(status='Nieuw')[:10]

    data = [{'id': onderzoek.onderzoek_id, 'titel': onderzoek.titel, 'organisatie': onderzoek.organisatie.bedrijfsnaam,
             'startdatum': onderzoek.startdatum, 'einddatum': onderzoek.einddatum, 'status': onderzoek.status}
            for onderzoek in
            recent_onderzoeken]

    return JsonResponse(data, safe=False)


def verwijder_onderzoek(request, onderzoek_id):
    onderzoek = get_object_or_404(Onderzoek, onderzoek_id=onderzoek_id)
    onderzoek.status = 'Afgekeurd'
    onderzoek.save()

    message = (
        f'Beste {onderzoek.organisatie.bedrijfsnaam},\n\n'
        f'Uw onderzoek is afgewezen.\n\n'
        f'Met vriendelijke groet,\n'
        'Het team van de Accessibility Hub'
    )

    send_mail(
        'Afkeuring van uw onderzoek',
        message,
        settings.EMAIL_HOST_USER,
        [onderzoek.organisatie.email],
        fail_silently=False,
    )
    return redirect('administrators:medewerkersportal')


def accepteer_onderzoek(request, onderzoek_id):
    onderzoek = get_object_or_404(Onderzoek, onderzoek_id=onderzoek_id)
    onderzoek.status = 'Geaccepteerd'
    onderzoek.save()

    message = (
        f'Beste {onderzoek.organisatie.bedrijfsnaam},\n\n'
        f'Uw onderzoek is geaccepteerd.\n\n'
        f'Met vriendelijke groet,\n'
        'Het team van de Accessibility Hub'
    )

    send_mail(
        'Goedkeuring van uw onderzoek',
        message,
        settings.EMAIL_HOST_USER,
        [onderzoek.organisatie.email],
        fail_silently=False,
    )
    return redirect('administrators:medewerkersportal')
