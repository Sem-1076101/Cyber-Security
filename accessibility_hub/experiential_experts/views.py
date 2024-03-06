from django.shortcuts import render, redirect
from administrators.models import Medewerker, Ervaringsdeskundige, Beperking
# from .forms import CreateExpertForm, LoginForm

# Authenticatie imports voor de login
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout 
# Create your views here.

def login(request):
    return render(request, 'login.html', {})

def signup(request):
    return render(request, 'signupExpert.html', {})