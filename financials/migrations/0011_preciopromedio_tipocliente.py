# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0006_tipocliente'),
        ('financials', '0010_pptipocliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='preciopromedio',
            name='tipoCliente',
            field=models.ForeignKey(default=b'', to='master.TipoCliente'),
            preserve_default=True,
        ),
    ]
