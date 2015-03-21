# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0006_controlingreso'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='controlingreso',
            name='reporte',
        ),
        migrations.RemoveField(
            model_name='controlingreso',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='ControlIngreso',
        ),
    ]
