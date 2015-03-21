# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0003_auto_20150305_1726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acceso',
            name='cargo',
        ),
        migrations.RemoveField(
            model_name='acceso',
            name='navegacion',
        ),
        migrations.DeleteModel(
            name='Acceso',
        ),
    ]
