from rest_framework import serializers
from .models import Onderzoek
from .models import Vraag
from .models import Onderzoekvraag
from django.contrib.auth.models import User

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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
