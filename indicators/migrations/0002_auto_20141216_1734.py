# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indicators', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='indicador',
            options={'verbose_name_plural': 'Indicadores'},
        ),
        migrations.AlterModelOptions(
            name='visualizacion',
            options={'verbose_name_plural': 'Visualizaciones'},
        ),
    ]
