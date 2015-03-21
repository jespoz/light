# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0020_fi_detallefrecuencia'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fi_detallefrecuencia',
            old_name='frecuencia',
            new_name='crudo',
        ),
        migrations.RemoveField(
            model_name='fi_detallefrecuencia',
            name='grupo',
        ),
        migrations.AddField(
            model_name='fi_detallefrecuencia',
            name='procesado',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
    ]
