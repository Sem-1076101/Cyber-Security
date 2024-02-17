from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'companies'

urlpatterns = [
    path('onderzoek/', views.onderzoek_lijst, name='onderzoek_lijst'),
    path('onderzoek/<int:onderzoek_id>', views.onderzoek_detail, name='onderzoek_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
