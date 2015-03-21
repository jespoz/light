# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0017_fi_mescurso'),
    ]

    operations = [
        migrations.AddField(
            model_name='fi_comparativo',
            name='mes_frecuencia',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fi_comparativo',
            name='mes_local',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fi_comparativo',
            name='mes_precio',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fi_comparativo',
            name='mes_ticket',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
    ]
