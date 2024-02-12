from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Medewerker
from django.forms.widgets import PasswordInput, TextInput

class CreateEmployeeForm(forms.ModelForm):
    wachtwoord = forms.CharField(label='wachtwoord', widget = forms.PasswordInput)
    class Meta:

        model = Medewerker
        fields = '__all__'

    def check_email(self):
        email = self.cleaned_data.get('email')

        if Medewerker.objects.filter(emailadres__iexact=email).exists():
            raise forms.ValidationError("Email is al in gebruik.")
        return email 
    
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())