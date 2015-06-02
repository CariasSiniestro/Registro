# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0012_auto_20150529_0423'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='workshop',
            options={'verbose_name': 'Taller', 'verbose_name_plural': 'Talleres'},
        ),
    ]
