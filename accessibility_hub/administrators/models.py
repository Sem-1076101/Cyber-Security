from django.db import models
from django.contrib.auth.hashers import make_password


class Onderzoeken(models.Model):
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
    organisatie_id = models.IntegerField()
    onderzoek_vragen_id = models.IntegerField()

    class Meta:
        db_table = 'onderzoeken'


class Medewerkers(models.Model):
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
    wachtwoord = models.CharField(max_length=255, default='')

    def save(self, *args, **kwargs):
        self.wachtwoord = make_password(self.wachtwoord)
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'medewerkers'
