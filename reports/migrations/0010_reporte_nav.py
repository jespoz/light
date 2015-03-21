# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0009_reporte_url_django'),
    ]

    operations = [
        migrations.AddField(
            model_name='reporte',
            name='nav',
            field=models.CharField(default=b'', max_length=100, null=True),
            preserve_default=True,
        ),
    ]
