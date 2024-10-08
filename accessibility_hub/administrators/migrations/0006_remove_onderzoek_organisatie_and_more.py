# Generated by Django 5.0.2 on 2024-03-08 12:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrators', '0005_merge_0004_alter_medewerker_test_0004_initial'),
        ('companies', '0012_alter_onderzoek_titel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='onderzoek',
            name='organisatie',
        ),
        migrations.AlterField(
            model_name='ervaringsdeskundige',
            name='onderzoek',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='companies.onderzoek'),
        ),
        migrations.RemoveField(
            model_name='medewerker',
            name='test',
        ),
        migrations.AddField(
            model_name='ervaringsdeskundige',
            name='benadering_keuze',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='ervaringsdeskundige',
            name='bericht_status',
            field=models.CharField(blank=True, default='null', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='ervaringsdeskundige',
            name='email_toezichthouder',
            field=models.CharField(blank=True, default='null', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='ervaringsdeskundige',
            name='naam_toezichthouder',
            field=models.CharField(blank=True, default='null', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='ervaringsdeskundige',
            name='telefoonnummer_toezichthouder',
            field=models.CharField(blank=True, default='null', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='ervaringsdeskundige',
            name='wachtwoord',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='ervaringsdeskundige',
            name='bijzonderheden',
            field=models.TextField(blank=True, default='null', null=True),
        ),
        migrations.AlterField(
            model_name='ervaringsdeskundige',
            name='hulpmiddelen',
            field=models.TextField(blank=True, default='null', null=True),
        ),
        migrations.AlterField(
            model_name='ervaringsdeskundige',
            name='telefoonnummer',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='medewerker',
            name='admin',
            field=models.BooleanField(),
        ),
        migrations.CreateModel(
            name='GoedkeuringErvaringsdeskundige',
            fields=[
                ('goedkeurings_id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.IntegerField(default=0)),
                ('datum_van_goed_keuring', models.DateField()),
                ('deskundige', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='administrators.ervaringsdeskundige')),
                ('medewerker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='administrators.medewerker')),
            ],
            options={
                'db_table': 'goedkeuring_ervaringsdeskundige',
            },
        ),
        migrations.DeleteModel(
            name='Organisatie',
        ),
        migrations.DeleteModel(
            name='Onderzoek',
        ),
    ]
