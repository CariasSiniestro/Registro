# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0010_auto_20150529_0418'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workshop',
            old_name='name',
            new_name='names',
        ),
    ]
