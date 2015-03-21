# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0009_formuladeingreso_tipocliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formuladeingreso',
            name='tipoCliente',
            field=models.ForeignKey(default=b'', to='master.TipoCliente', null=True),
            preserve_default=True,
        ),
    ]
