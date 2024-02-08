from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Medewerker

class CreateEmployeeForm(forms.ModelForm):

    class Meta:

        model = Medewerker
        fields = '__all__'