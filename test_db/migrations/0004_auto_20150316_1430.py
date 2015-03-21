# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_db', '0003_localcompleto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localcompleto',
            name='preventa',
            field=models.CharField(default=b'', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='localcompleto',
            name='supervisor',
            field=models.CharField(default=b'', max_length=200),
            preserve_default=True,
        ),
    ]
