from django.db import models

class Onderzoek(models.Model):
    titel = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    beschikbaar = models.BooleanField(default=False)
    beschrijving = models.TextField()
    datum_vanaf = models.DateField()
    datum_tot = models.DateField()
    type_onderzoek = models.CharField(max_length=50)
    locatie = models.CharField(max_length=100)
    beloning = models.CharField(max_length=100)
    doelgroep_beperking = models.CharField(max_length=100)
    organisatie = models.CharField(max_length=100)
    
    def __str__(self):
        return self.titel