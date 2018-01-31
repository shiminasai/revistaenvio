# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-11-17 21:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulos',
            fields=[
                ('idarticulo', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(blank=True, max_length=255, null=True)),
                ('numero', models.IntegerField(blank=True, null=True)),
                ('ididioma', models.CharField(blank=True, max_length=2, null=True)),
                ('autornota', models.TextField(blank=True, null=True)),
                ('cambio', models.TextField(blank=True, null=True)),
                ('texto', models.TextField(blank=True, null=True)),
                ('codigoml', models.IntegerField(blank=True, null=True)),
                ('nota', models.TextField(blank=True, null=True)),
                ('textoidx', models.TextField(blank=True, null=True)),
                ('idxtexto', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'articulos',
            },
        ),
        migrations.CreateModel(
            name='Articulotemas',
            fields=[
                ('ididioma', models.CharField(blank=True, max_length=2, null=True)),
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('idarticulo', models.ForeignKey(db_column='idarticulo', on_delete=django.db.models.deletion.DO_NOTHING, to='revista.Articulos')),
            ],
            options={
                'db_table': 'articulotemas',
            },
        ),
        migrations.CreateModel(
            name='Autores',
            fields=[
                ('idautor', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=150, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('titulo', models.CharField(blank=True, max_length=50, null=True)),
                ('cargo', models.TextField(blank=True, null=True)),
                ('nota', models.TextField(blank=True, null=True)),
                ('nombre_it', models.CharField(blank=True, max_length=150, null=True)),
                ('nombre_en', models.CharField(blank=True, max_length=150, null=True)),
                ('nombre_es', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'db_table': 'autores',
            },
        ),
        migrations.CreateModel(
            name='Enlaces',
            fields=[
                ('idenlace', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.TextField(blank=True, null=True)),
                ('texto', models.TextField(blank=True, null=True)),
                ('idarticulo', models.ForeignKey(blank=True, db_column='idarticulo', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='revista.Articulos')),
            ],
            options={
                'db_table': 'enlaces',
            },
        ),
        migrations.CreateModel(
            name='Envio',
            fields=[
                ('idenvio', models.AutoField(primary_key=True, serialize=False)),
                ('envio', models.CharField(blank=True, max_length=500, null=True)),
                ('institucion', models.CharField(blank=True, max_length=500, null=True)),
                ('direccion', models.CharField(blank=True, max_length=500, null=True)),
                ('email', models.CharField(blank=True, max_length=500, null=True)),
                ('apdo', models.CharField(blank=True, max_length=50, null=True)),
                ('telefono', models.CharField(blank=True, max_length=50, null=True)),
                ('fax', models.CharField(blank=True, max_length=50, null=True)),
                ('ciudad', models.CharField(blank=True, max_length=100, null=True)),
                ('codigo', models.CharField(blank=True, max_length=50, null=True)),
                ('idpais', models.CharField(blank=True, max_length=2, null=True)),
                ('nueva', models.NullBooleanField()),
                ('idioma', models.CharField(blank=True, max_length=10, null=True)),
                ('forma_pago', models.CharField(blank=True, max_length=2, null=True)),
                ('ttipo', models.CharField(blank=True, max_length=4, null=True)),
                ('tnumero', models.CharField(blank=True, max_length=50, null=True)),
                ('texpira', models.CharField(blank=True, max_length=10, null=True)),
                ('tnombre', models.CharField(blank=True, max_length=200, null=True)),
                ('fecha', models.DateTimeField(blank=True, null=True)),
                ('nombre', models.CharField(blank=True, max_length=500, null=True)),
                ('suscripcion', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'db_table': 'envio',
            },
        ),
        migrations.CreateModel(
            name='ExportArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idarticulo', models.IntegerField(blank=True, null=True)),
                ('numero', models.IntegerField(blank=True, null=True)),
                ('ididioma', models.CharField(blank=True, max_length=2, null=True)),
                ('idzona', models.CharField(blank=True, max_length=2, null=True)),
                ('idautor', models.IntegerField(blank=True, null=True)),
                ('cambio', models.TextField(blank=True, null=True)),
                ('codigoml', models.IntegerField(blank=True, null=True)),
                ('textoidx', models.TextField(blank=True, null=True)),
                ('idxtexto', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'export_article',
            },
        ),
        migrations.CreateModel(
            name='ExportRevistas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volumen', models.IntegerField(blank=True, null=True)),
                ('ano', models.IntegerField(blank=True, null=True)),
                ('mes', models.IntegerField(blank=True, null=True)),
                ('numero', models.IntegerField(blank=True, null=True)),
                ('ididioma', models.CharField(blank=True, max_length=2, null=True)),
                ('nota', models.TextField(blank=True, null=True)),
                ('color', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'export_revistas',
            },
        ),
        migrations.CreateModel(
            name='ExportRevistasDetalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('master_id', models.IntegerField(blank=True, null=True)),
                ('titulo', models.CharField(blank=True, max_length=255, null=True)),
                ('ididioma', models.CharField(blank=True, max_length=2, null=True)),
                ('autornota', models.TextField(blank=True, null=True)),
                ('texto', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'export_revistas_detalle',
            },
        ),
        migrations.CreateModel(
            name='Idiomas',
            fields=[
                ('ididioma', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('idioma', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'idiomas',
            },
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('idimagen', models.AutoField(primary_key=True, serialize=False)),
                ('imagen', models.CharField(blank=True, max_length=200, null=True)),
                ('idarticulo', models.ForeignKey(blank=True, db_column='idarticulo', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='revista.Articulos')),
            ],
            options={
                'db_table': 'imagen',
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('idpais', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('pais', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'pais',
            },
        ),
        migrations.CreateModel(
            name='PgTsCfg',
            fields=[
                ('ts_name', models.TextField(primary_key=True, serialize=False)),
                ('prs_name', models.TextField()),
                ('locale', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pg_ts_cfg',
            },
        ),
        migrations.CreateModel(
            name='PgTsCfgmap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ts_name', models.TextField()),
                ('tok_alias', models.TextField()),
                ('dict_name', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pg_ts_cfgmap',
            },
        ),
        migrations.CreateModel(
            name='Revistas',
            fields=[
                ('volumen', models.IntegerField(blank=True, null=True)),
                ('ano', models.IntegerField(blank=True, null=True)),
                ('mes', models.IntegerField(blank=True, null=True)),
                ('numero', models.IntegerField()),
                ('nota', models.TextField(blank=True, null=True)),
                ('color', models.IntegerField(blank=True, null=True)),
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('ididioma', models.ForeignKey(db_column='ididioma', on_delete=django.db.models.deletion.DO_NOTHING, to='revista.Idiomas')),
            ],
            options={
                'db_table': 'revistas',
            },
        ),
        migrations.CreateModel(
            name='Temas',
            fields=[
                ('idtema', models.AutoField(primary_key=True, serialize=False)),
                ('tema', models.CharField(blank=True, max_length=150, null=True)),
                ('tema_it', models.CharField(blank=True, max_length=150, null=True)),
                ('tema_en', models.CharField(blank=True, max_length=150, null=True)),
                ('tema_es', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'db_table': 'temas',
            },
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('idtipo', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('tipo', models.CharField(blank=True, max_length=500, null=True)),
                ('precio', models.CharField(blank=True, max_length=50, null=True)),
                ('tipo_es', models.CharField(blank=True, max_length=500, null=True)),
                ('tipo_en', models.CharField(blank=True, max_length=500, null=True)),
                ('tipo_it', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'tipo',
            },
        ),
        migrations.CreateModel(
            name='Zonas',
            fields=[
                ('idzona', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('zona', models.CharField(blank=True, max_length=50, null=True)),
                ('relevancia', models.IntegerField(blank=True, null=True)),
                ('zona_it', models.CharField(blank=True, max_length=50, null=True)),
                ('zona_en', models.CharField(blank=True, max_length=50, null=True)),
                ('zona_es', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'zonas',
            },
        ),
        migrations.AlterUniqueTogether(
            name='pgtscfgmap',
            unique_together=set([('ts_name', 'tok_alias')]),
        ),
        migrations.AddField(
            model_name='envio',
            name='idtipo',
            field=models.ForeignKey(blank=True, db_column='idtipo', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='revista.Tipo'),
        ),
        migrations.AddField(
            model_name='articulotemas',
            name='idtema',
            field=models.ForeignKey(db_column='idtema', on_delete=django.db.models.deletion.DO_NOTHING, to='revista.Temas'),
        ),
        migrations.AddField(
            model_name='articulos',
            name='idautor',
            field=models.ForeignKey(blank=True, db_column='idautor', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='revista.Autores'),
        ),
        migrations.AddField(
            model_name='articulos',
            name='idzona',
            field=models.ForeignKey(blank=True, db_column='idzona', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='revista.Zonas'),
        ),
        migrations.AddField(
            model_name='articulos',
            name='revista',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='revista.Revistas'),
        ),
    ]
