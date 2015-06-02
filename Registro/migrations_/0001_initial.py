# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=500, verbose_name=b'Description')),
                ('order', models.CharField(max_length=b'10', verbose_name=b'Orden')),
            ],
            options={
                'db_table': 'Price',
                'verbose_name': 'Premio',
                'verbose_name_plural': 'Premios',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=75, verbose_name=b'Nombre')),
                ('last_name', models.CharField(max_length=75, verbose_name=b'Apellido')),
                ('licence', models.CharField(max_length=75, verbose_name=b'Carnet')),
                ('assistence', models.BooleanField(default=False, verbose_name=b'Asistencia')),
                ('solvence', models.BooleanField(default=False, verbose_name=b'Solvente')),
                ('Winner', models.BooleanField(default=False, verbose_name=b'Ganador')),
                ('Payment', models.FloatField(max_length=10, verbose_name=b'Abono')),
                ('Price_Winned', models.ForeignKey(blank=True, editable=False, to='Registro.Price', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Nombre')),
                ('manager', models.CharField(max_length=50, verbose_name=b'Apellido')),
                ('max_capacity', models.IntegerField(max_length=3, verbose_name=b'Carnet')),
                ('registered', models.IntegerField(max_length=3, verbose_name=b'Cupo')),
            ],
            options={
                'db_table': 'Workshop',
                'verbose_name': 'Taller',
                'verbose_name_plural': 'Talleres',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='student',
            name='Workshop_assigned',
            field=models.ForeignKey(blank=True, to='Registro.Workshop', null=True),
            preserve_default=True,
        ),
    ]
