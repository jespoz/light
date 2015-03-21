# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imports', '0007_ventacompleta_periodo'),
    ]

    operations = [
        migrations.AddField(
            model_name='ventacompleta',
            name='unidad',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
    ]
