# Generated by Django 4.2.2 on 2023-07-04 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WhatApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='estatus',
            field=models.IntegerField(),
        ),
    ]
