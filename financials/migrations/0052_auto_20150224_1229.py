# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financials', '0051_costomerchacum'),
    ]

    operations = [
        migrations.RenameField(
            model_name='costoventas',
            old_name='costo',
            new_name='nacional',
        ),
        migrations.AddField(
            model_name='costoventas',
            name='sucursal',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='costoventas',
            name='zonal',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
    ]
