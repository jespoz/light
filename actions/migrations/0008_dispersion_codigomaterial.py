# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0007_dispersion'),
    ]

    operations = [
        migrations.AddField(
            model_name='dispersion',
            name='codigoMaterial',
            field=models.IntegerField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
    ]
