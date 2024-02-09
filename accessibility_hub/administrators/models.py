from django.db import models
from django import forms
from django.contrib.auth.hashers import make_password


class Onderzoek(models.Model):
    onderzoek_id = models.AutoField(primary_key=True)
    titel = models.CharField(max_length=255)
    status = models.CharField(max_length=100)
    beschikbaar = models.CharField(max_length=50)
    beschrijving = models.CharField(max_length=255)
    datum_vanaf = models.DateField()
    datum_tot = models.DateField()
    type_onderzoek = models.CharField(max_length=50)
    locatie = models.CharField(max_length=255)
    met_beloning = models.BooleanField()
    beloning = models.TextField(null=True, blank=True)
    doelgroep_leeftijd_van = models.IntegerField()
    doelgroep_leeftijd_tot = models.IntegerField()
    doelgroep_beperking = models.CharField(max_length=100)
    onderzoek_vragen_id = models.IntegerField()
    organisatie = models.ForeignKey(
        'Organisatie', on_delete=models.SET_NULL, null=True
    )

    class Meta:
        db_table = 'onderzoeken'


class Medewerker(models.Model):
    medewerker_id = models.AutoField(primary_key=True)
    voornaam = models.CharField(max_length=255)
    achternaam = models.CharField(max_length=100)
    gebruikersnaam = models.CharField(max_length=255, default='')
    wachtwoord = models.CharField(max_length=255)
    emailadres = models.CharField(max_length=255)
    postcode = models.CharField(max_length=6)
    huisnummer = models.IntegerField()
    geslacht = models.CharField(max_length=10) 
    telefoonnummer = models.CharField(max_length=15)
    geboortedatum = models.DateField()
    admin = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.wachtwoord = make_password(self.wachtwoord)
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'medewerkers'


class Organisatie(models.Model):
    organisatie_id = models.AutoField(primary_key=True)
    naam = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    website = models.URLField(max_length=200)
    beschrijving = models.TextField()
    contactpersoon = models.CharField(max_length=255)
    emailadres = models.EmailField(max_length=255)
    telefoonnummer = models.CharField(max_length=15)
    overige_details = models.TextField()

    class Meta:
        db_table = 'organisaties'


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
    onderzoek = models.ForeignKey(
        'Onderzoek', on_delete=models.SET_NULL, blank=True, null=True
    )

    class Meta:
        db_table = 'ervaringsdeskundigen'


class Beperking(models.Model):
    beperking_id = models.AutoField(primary_key=True)
    beperking = models.CharField(max_length=255)
    categorie = models.CharField(max_length=255)

    class Meta:
        db_table = 'beperkingen'
