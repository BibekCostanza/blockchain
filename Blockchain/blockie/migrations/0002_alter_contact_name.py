# Generated by Django 4.1.6 on 2023-04-28 01:49

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=100, verbose_name=django.contrib.auth.models.User),
        ),
    ]
