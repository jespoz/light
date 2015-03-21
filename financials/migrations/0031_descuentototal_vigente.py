# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financials', '0030_pesotipocliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='descuentototal',
            name='vigente',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
    ]
