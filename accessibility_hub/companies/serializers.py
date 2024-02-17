from rest_framework import serializers
from .models import Onderzoek
from .models import Vraag
from .models import Onderzoekvraag

class OnderzoekSerializer(serializers.ModelSerializer):
    class Meta:
        model = Onderzoek
        fields = '__all__'


class VraagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vraag
        fields = '__all__'


class OnderzoekvraagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Onderzoekvraag
        fields = '__all__'
