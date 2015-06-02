# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0014_auto_20150529_0427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Payment',
            field=models.FloatField(max_length=10, verbose_name=b'Abono'),
        ),
    ]
