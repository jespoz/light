# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financials', '0046_auto_20150120_0847'),
    ]

    operations = [
        migrations.AddField(
            model_name='costoapertura',
            name='peso',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
    ]
