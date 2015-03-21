# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0008_reporte_icono'),
    ]

    operations = [
        migrations.AddField(
            model_name='reporte',
            name='url_django',
            field=models.CharField(default=b'', max_length=100, null=True),
            preserve_default=True,
        ),
    ]
