# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-11-20 22:43
from __future__ import unicode_literals

from django.db import migrations


def trasnferir_idioma(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Articulos = apps.get_model('revista', 'Articulos')
    Idiomas = apps.get_model('revista', 'Idiomas')
    for articulo in Articulos.objects.all():
        idioma2, created = Idiomas.objects.get_or_create(id=articulo.idioma)
        articulo.ididioma = idioma2
        articulo.save()


class Migration(migrations.Migration):

    dependencies = [
        ('revista', '0008_transfer_color'),
    ]

    operations = [
        migrations.RunPython(trasnferir_idioma),
    ]
