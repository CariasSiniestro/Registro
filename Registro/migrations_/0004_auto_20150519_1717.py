# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0003_auto_20150516_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshop',
            name='registered',
            field=models.IntegerField(verbose_name=b'Registrados', max_length=3, null=True, editable=False, blank=True),
        ),
    ]
