from .models import Onderzoek, Medewerker, Organisatie, Ervaringsdeskundige, Beperking

# Authenticatie imports voor de login
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout 

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Medewerker
from django.forms.widgets import PasswordInput, TextInput


