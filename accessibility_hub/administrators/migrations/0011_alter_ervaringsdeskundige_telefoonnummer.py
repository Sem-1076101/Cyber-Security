# Generated by Django 5.0.1 on 2024-03-01 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrators', '0010_ervaringsdeskundige_benadering_keuze_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ervaringsdeskundige',
            name='telefoonnummer',
            field=models.IntegerField(blank=True, max_length=15, null=True),
        ),
    ]
