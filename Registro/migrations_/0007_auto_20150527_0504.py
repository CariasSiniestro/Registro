# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0006_price_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Payment',
            field=models.FloatField(max_length=5, verbose_name=b'Abono'),
        ),
    ]
