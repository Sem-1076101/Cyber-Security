# Generated by Django 5.0.1 on 2024-02-19 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organisatie',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='organisatie',
            name='last_name',
        ),
    ]
