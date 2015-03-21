# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financials', '0034_descuentofacturado'),
    ]

    operations = [
        migrations.AddField(
            model_name='descuento',
            name='tipoPedido',
            field=models.CharField(default=b'', max_length=100, null=True),
            preserve_default=True,
        ),
    ]
