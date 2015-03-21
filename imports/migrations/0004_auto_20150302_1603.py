# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imports', '0003_historialcreacionreporte'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historialcreacionreporte',
            name='actualizacion',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
