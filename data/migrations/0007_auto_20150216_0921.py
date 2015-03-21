# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_auto_20150212_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='fi_totales',
            name='var_kilo',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fi_totales',
            name='var_neto',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
    ]
