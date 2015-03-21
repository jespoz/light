# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0014_auto_20150104_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='ccnivel2',
            name='seudo',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
    ]
