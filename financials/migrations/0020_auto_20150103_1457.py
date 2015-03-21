# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0007_cadena'),
        ('financials', '0019_descuentocadena'),
    ]

    operations = [
        migrations.AddField(
            model_name='descuento',
            name='cliente',
            field=models.CharField(default=b'', max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='descuento',
            name='rut',
            field=models.CharField(default=b'', max_length=20, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='descuento',
            name='sector',
            field=models.ForeignKey(to='master.Sector', null=True),
            preserve_default=True,
        ),
    ]
