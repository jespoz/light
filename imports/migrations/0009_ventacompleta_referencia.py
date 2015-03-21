# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imports', '0008_ventacompleta_unidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='ventacompleta',
            name='referencia',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
