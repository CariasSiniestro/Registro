# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0007_auto_20150527_0504'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Estudiante', 'verbose_name_plural': 'Estudiantes'},
        ),
    ]
