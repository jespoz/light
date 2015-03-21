# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_db', '0004_auto_20150316_1430'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='localcompleto',
            name='preventa',
        ),
        migrations.RemoveField(
            model_name='localcompleto',
            name='supervisor',
        ),
    ]
