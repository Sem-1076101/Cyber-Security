from django.db import models


# Create your models here.

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
        db_table = 'organisatie_onderzoeken'

    def __str__(self):
        return self.titel


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
        db_table = 'organisatie_organisaties'

    def __str__(self):
        return self.naam
