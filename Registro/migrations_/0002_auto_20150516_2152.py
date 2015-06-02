# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Winner',
            field=models.BooleanField(default=False, verbose_name=b'Ganador', editable=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='assistence',
            field=models.BooleanField(default=False, verbose_name=b'Asistencia', editable=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='solvence',
            field=models.BooleanField(default=False, verbose_name=b'Solvente', editable=False),
        ),
    ]
