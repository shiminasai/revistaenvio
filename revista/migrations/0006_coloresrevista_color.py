# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-27 17:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revista', '0005_auto_20161027_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='coloresrevista',
            name='color',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]