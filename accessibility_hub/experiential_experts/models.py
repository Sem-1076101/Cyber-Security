from django.db import models
from administrators.models import Onderzoek

class Onderzoek(models.Model):
    class Meta:
        model = Onderzoek
        fields = ('titel', 'status', 'beschikbaar', 'beschrijving', 'datum_vanaf', 'datum_tot', 'type_onderzoek', 'locatie', 'beloning', 'doelgroep_beperking', 'organisatie')

    def __str__(self):
        return self.titel