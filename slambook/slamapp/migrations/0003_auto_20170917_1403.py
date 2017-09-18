# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-17 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slamapp', '0002_auto_20170917_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='city',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='user_profile',
            name='country',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='user_profile',
            name='day',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AddField(
            model_name='user_profile',
            name='gender',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='user_profile',
            name='month',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AddField(
            model_name='user_profile',
            name='year',
            field=models.CharField(blank=True, max_length=5),
        ),
    ]