# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0013_clasescoste_nivel3'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ccnivel4',
            name='nivel3',
        ),
        migrations.DeleteModel(
            name='CCNivel4',
        ),
    ]
