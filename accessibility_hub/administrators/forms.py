from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Medewerker
from django.forms.widgets import PasswordInput, TextInput
from django.core.exceptions import ValidationError

class CreateEmployeeForm(forms.ModelForm):
    wachtwoord = forms.CharField(label='Wachtwoord', widget = forms.PasswordInput)
    # firstName = forms.CharField(label='Voornaam', max_length=100)
    # lastName = forms.CharField(label='Achternaam', max_length=100)
    # email = forms.EmailField(label='E-mailadres')
    # gender = forms.CharField(label='Geslacht', max_length=10)
    # birthday = forms.DateField(label='Geboortedatum')
    # zipCode = forms.CharField(label='Postcode', max_length=6)
    # housenumber = forms.IntegerField(label='Huisnummer')
    # admin = forms.BooleanField()
    
    
    class Meta:
        model = Medewerker
        fields = ('voornaam', 'achternaam', 'gebruikersnaam', 'wachtwoord', 'emailadres', 'postcode', 'huisnummer', 'geslacht', 'geboortedatum', 'admin')
    
class LoginForm(forms.Form):
    gebruikersnaam = forms.CharField(label='Gebruikersnaam', max_length=100)
    wachtwoord = forms.CharField(label='wachtwoord', widget = forms.PasswordInput)