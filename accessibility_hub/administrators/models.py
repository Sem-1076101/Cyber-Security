from django.db import models


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
