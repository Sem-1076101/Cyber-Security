from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Organisatie(AbstractUser):
    bedrijfsnaam = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True, db_column='email')
    token = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=255, default='Nieuw')
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'organisaties'
