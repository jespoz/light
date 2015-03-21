# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financials', '0041_pesodesccallfact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='descuentocadena',
            name='cadena',
        ),
        migrations.RemoveField(
            model_name='descuentocadena',
            name='oficina',
        ),
        migrations.RemoveField(
            model_name='descuentocadena',
            name='periodo',
        ),
        migrations.DeleteModel(
            name='DescuentoCadena',
        ),
        migrations.RemoveField(
            model_name='descuentosector',
            name='oficina',
        ),
        migrations.RemoveField(
            model_name='descuentosector',
            name='periodo',
        ),
        migrations.RemoveField(
            model_name='descuentosector',
            name='sector',
        ),
        migrations.DeleteModel(
            name='DescuentoSector',
        ),
    ]
