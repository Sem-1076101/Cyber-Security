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
    
class LoginForm(forms.ModelForm):
    wachtwoord = forms.CharField(label='wachtwoord', widget = forms.PasswordInput)
    class Meta: 
        model = Medewerker
        fields = ('gebruikersnaam', 'wachtwoord')