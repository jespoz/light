# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0005_analisisdescuentoapertura'),
    ]

    operations = [
        migrations.RenameField(
            model_name='analisisdescuentoapertura',
            old_name='trs',
            new_name='tres',
        ),
    ]
