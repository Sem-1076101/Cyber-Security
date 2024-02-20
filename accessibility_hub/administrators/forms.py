from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Medewerker
from django.forms.widgets import PasswordInput, TextInput
from django.core.exceptions import ValidationError

class CreateEmployeeForm(forms.ModelForm):
    wachtwoord = forms.CharField(label='wachtwoord', widget = forms.PasswordInput)
    class Meta:

        model = Medewerker
        fields = '__all__'
        # ['voornaam', 'achternaam', 'gebruikersnaam', 'wachtwoord', 'emailadres', 'postcode', 'huisnummer', 'geslacht', 'telefoonnummer', 'geboortedatum', 'admin'] 
    
class LoginForm(forms.Form):
    gebruikersnaam = forms.CharField(label='Gebruikersnaam', max_length=100)
    wachtwoord = forms.CharField(label='wachtwoord', widget = forms.PasswordInput)