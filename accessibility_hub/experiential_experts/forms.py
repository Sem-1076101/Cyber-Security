from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from administrators.models import Ervaringsdeskundige
from django.forms.widgets import PasswordInput, TextInput
from django.core.exceptions import ValidationError

class CreateExpertForm(forms.Form):
    firstName = forms.CharField(label='Voornaam')
    lastName = forms.CharField(label='Achternaam')
    password = forms.CharField(label='Wachtwoord', widget = forms.PasswordInput)
    email = forms.CharField(label='Email')
    gender = forms.CharField(label='Geslacht')
    birthday = forms.CharField(label='Geboortedatum')
    zipcode = forms.CharField(label='Postcode')
    disability = forms.CharField(label='Beperking')
    tools = forms.CharField(label='Gebruikte hulpmiddelen')
    particulars = forms.CharField(label='Bijzonderheden')
    supervisor = forms.CharField(label='Toezichthouder')
    supervisorName = forms.CharField(label='Toezichthouder naam', default='NULL')
    email_supervisor = forms.CharField(label='Toezichthouder email', default='NULL')
    phonenumber_supervisor = forms.CharField(label='Toezichthouder telefoonnummer', default='NULL')
    approach_choice = forms.CharField(label='Benadering keuze')


    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

class LoginFormExpert(forms.Form):
    gebruikersnaam = forms.CharField(label='Gebruikersnaam', max_length=100)
    wachtwoord = forms.CharField(label='wachtwoord', widget = forms.PasswordInput)