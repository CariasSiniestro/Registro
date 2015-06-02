# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0004_auto_20150519_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshop',
            name='registered',
            field=models.IntegerField(default=0, verbose_name=b'Registrados', max_length=3, editable=False),
        ),
    ]
