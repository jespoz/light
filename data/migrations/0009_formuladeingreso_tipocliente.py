# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0019_periodo_tipoperiodo'),
        ('data', '0008_fi_comparativo'),
    ]

    operations = [
        migrations.AddField(
            model_name='formuladeingreso',
            name='tipoCliente',
            field=models.ForeignKey(default=b'', to='master.TipoCliente'),
            preserve_default=True,
        ),
    ]
