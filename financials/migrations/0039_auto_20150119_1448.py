# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financials', '0038_pesodescuentocall'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pesodescuentocall',
            name='total',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
    ]
