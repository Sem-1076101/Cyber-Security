from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

app_name = 'administrators'
# LoginView.as_view()
urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('portal/', views.portal, name='medewerkers portal'),
    path('medewerker/', views.medewerker, name='medewerker'),
]
 