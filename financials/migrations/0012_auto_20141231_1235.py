# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financials', '0011_preciopromedio_tipocliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preciopromedio',
            name='tipoCliente',
            field=models.ForeignKey(default=b'', to='master.TipoCliente', null=True),
            preserve_default=True,
        ),
    ]
