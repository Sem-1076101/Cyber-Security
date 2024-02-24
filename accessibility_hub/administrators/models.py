from django.db import models
from companies.models import Organisatie
from django.contrib.auth.hashers import make_password


class Medewerker(models.Model):
    medewerker_id = models.AutoField(primary_key=True)
    voornaam = models.CharField(max_length=255)
    achternaam = models.CharField(max_length=100)
    postcode = models.CharField(max_length=6)
    huisnummer = models.IntegerField()
    geslacht = models.CharField(max_length=10)
    emailadres = models.CharField(max_length=255)
    telefoonnummer = models.CharField(max_length=15)
    geboortedatum = models.DateField()
    admin = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    gebruikersnaam = models.CharField(max_length=255, default='')
    wachtwoord = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.wachtwoord = make_password(self.wachtwoord)
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'medewerkers'


class Ervaringsdeskundige(models.Model):
    deskundige_id = models.AutoField(primary_key=True)
    voornaam = models.CharField(max_length=255, blank=True, null=True)
    achternaam = models.CharField(max_length=255, blank=True, null=True)
    geboortedatum = models.DateField(blank=True, null=True)
    telefoonnummer = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    geslacht = models.CharField(max_length=10, blank=True, null=True)
    postcode = models.CharField(max_length=6, blank=True, null=True)
    huisnummer = models.IntegerField(blank=True, null=True)
    soort_beperking = models.TextField(blank=True, null=True)
    hulpmiddelen = models.TextField(blank=True, null=True)
    bijzonderheden = models.TextField(blank=True, null=True)
    account_status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    beperking = models.ForeignKey(
        'Beperking', on_delete=models.SET_NULL, blank=True, null=True
    )
    # onderzoek = models.ForeignKey(
    #     'Onderzoek', on_delete=models.SET_NULL, blank=True, null=True
    # )

    class Meta:
        db_table = 'ervaringsdeskundigen'


class Beperking(models.Model):
    beperking_id = models.AutoField(primary_key=True)
    beperking = models.CharField(max_length=255)
    categorie = models.CharField(max_length=255)

    class Meta:
        db_table = 'beperkingen'
