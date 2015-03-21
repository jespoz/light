# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_fi_totales'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formuladeingreso',
            name='cliente',
            field=models.IntegerField(max_length=20),
            preserve_default=True,
        ),
    ]
