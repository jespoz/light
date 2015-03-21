# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0008_dispersion_codigomaterial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dispersion',
            name='codigoMaterial',
        ),
        migrations.AddField(
            model_name='dispersion',
            name='material',
            field=models.CharField(default=b'', max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
    ]
