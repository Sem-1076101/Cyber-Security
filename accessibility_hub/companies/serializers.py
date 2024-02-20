from rest_framework import serializers
from .models import Organisatie


class OrganisatieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisatie
        fields = ['id', 'bedrijfsnaam', 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        email = validated_data.get('email')
        if Organisatie.objects.filter(email=email).exists():
            raise serializers.ValidationError("E-mailadres is al in gebruik")

        wachtwoord = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if wachtwoord is not None:
            instance.set_password(wachtwoord)
        instance.save()
        return instance
