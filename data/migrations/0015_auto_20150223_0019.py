# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0014_iconoslocales'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fi_comparativo',
            name='mes_frecuencia',
        ),
        migrations.RemoveField(
            model_name='fi_comparativo',
            name='mes_local',
        ),
        migrations.RemoveField(
            model_name='fi_comparativo',
            name='mes_precio',
        ),
        migrations.RemoveField(
            model_name='fi_comparativo',
            name='mes_ticket',
        ),
    ]
