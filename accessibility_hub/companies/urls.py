from django.urls import path
from .views import Register, Login, Research

app_name = 'companies'

urlpatterns = [
    path('register/', Register.as_view()),
    path('login/', Login.as_view()),
    path('onderzoek/', Research.as_view()),
]
