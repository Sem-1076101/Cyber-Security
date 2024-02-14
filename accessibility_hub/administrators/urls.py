from django.urls import path
from . import views

app_name = 'administrators'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('portal/', views.portal, name='medewerkersportal'),
    path('medewerker/<int:medewerker_id>/', views.medewerker, name='medewerker'),
    path('verwijder_medewerker/<int:medewerker_id>/', views.verwijder_medewerker, name='verwijder_medewerker'),
]
