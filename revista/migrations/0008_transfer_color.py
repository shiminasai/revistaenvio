# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-11-20 21:57
from __future__ import unicode_literals

from django.db import migrations


def trasnferir_color(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Revistas = apps.get_model('revista', 'Revistas')
    Colores = apps.get_model('revista', 'ColoresRevista')
    for revista in Revistas.objects.all():
        colors, created = Colores.objects.get_or_create(color1=revista.color)
        revista.colores = colors
        revista.save()


class Migration(migrations.Migration):

    dependencies = [
        ('revista', '0007_auto_20171120_2148'),
    ]

    operations = [
        migrations.RunPython(trasnferir_color),
    ]
