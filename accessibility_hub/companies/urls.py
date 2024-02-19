from django.urls import path
from .views import Register, Login

app_name = 'companies'

urlpatterns = [
    path('register/', Register.as_view()),
    path('login/', Login.as_view()),
]
