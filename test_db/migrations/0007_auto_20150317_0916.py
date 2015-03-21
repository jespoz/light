# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_db', '0006_auto_20150316_1431'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Interlocutor',
        ),
        migrations.RemoveField(
            model_name='localcompleto',
            name='sector',
        ),
        migrations.DeleteModel(
            name='LocalCompleto',
        ),
        migrations.RemoveField(
            model_name='localsector',
            name='sector',
        ),
        migrations.DeleteModel(
            name='LocalSector',
        ),
    ]
