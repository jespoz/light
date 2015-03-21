# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0008_auto_20150103_1606'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ccnivel2',
            name='nivel1',
        ),
        migrations.DeleteModel(
            name='CCNivel1',
        ),
        migrations.RemoveField(
            model_name='ccnivel3',
            name='nivel2',
        ),
        migrations.DeleteModel(
            name='CCNivel2',
        ),
        migrations.RemoveField(
            model_name='ccnivel4',
            name='nivel3',
        ),
        migrations.DeleteModel(
            name='CCNivel3',
        ),
        migrations.DeleteModel(
            name='CCNivel4',
        ),
    ]
