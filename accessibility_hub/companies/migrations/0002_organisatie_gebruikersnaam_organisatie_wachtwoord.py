# Generated by Django 5.0.1 on 2024-02-18 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisatie',
            name='gebruikersnaam',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organisatie',
            name='wachtwoord',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
