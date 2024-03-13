from django.urls import path
from experiential_experts import views

app_name = 'ervaringsdeskundige'

# Create your views here.

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('onderzoek-overzicht/', views.onderzoek_overzicht, name='onderzoek_overzicht'),
    path('inschrijvingen/', views.inschrijvingen, name='inschrijvingen'),
    path('uitschrijvingen/', views.uitschrijvingen, name='uitschrijvingen')
]
