# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0010_reporte_nav'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reporte',
            name='nav',
        ),
    ]
