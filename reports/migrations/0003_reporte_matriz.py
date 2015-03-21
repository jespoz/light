# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_reporte_sap'),
    ]

    operations = [
        migrations.AddField(
            model_name='reporte',
            name='matriz',
            field=models.FileField(null=True, upload_to=b'/matrices/', blank=True),
            preserve_default=True,
        ),
    ]
