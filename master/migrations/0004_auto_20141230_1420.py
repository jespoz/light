# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0003_zonaventas'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='zonaventas',
            options={'verbose_name': 'Zona de Ventas', 'verbose_name_plural': 'Zonas de Ventas'},
        ),
        migrations.AddField(
            model_name='oficinaventas',
            name='zona',
            field=models.ForeignKey(default=b'', to='master.ZonaVentas', null=True),
            preserve_default=True,
        ),
    ]
