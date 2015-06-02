# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0002_auto_20150516_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshop',
            name='manager',
            field=models.CharField(max_length=50, verbose_name=b'Encargado'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='max_capacity',
            field=models.IntegerField(max_length=3, verbose_name=b'Capacidad'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='registered',
            field=models.IntegerField(max_length=3, verbose_name=b'Registrados'),
        ),
    ]
