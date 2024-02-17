from django.contrib import admin
from .models import Onderzoek, Organisatie, Vraag, Onderzoekvraag

# Register your models here.

admin.site.register(Onderzoek)
admin.site.register(Organisatie)
admin.site.register(Vraag)
admin.site.register(Onderzoekvraag)
