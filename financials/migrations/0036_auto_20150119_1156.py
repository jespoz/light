# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financials', '0035_descuento_tipopedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='descuentosucursal',
            name='peso_facturado',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='descuentosucursal',
            name='peso_pedido',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
    ]
