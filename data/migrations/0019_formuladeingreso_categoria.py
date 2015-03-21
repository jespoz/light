# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0022_categoriacliente'),
        ('data', '0018_auto_20150223_0147'),
    ]

    operations = [
        migrations.AddField(
            model_name='formuladeingreso',
            name='categoria',
            field=models.ForeignKey(default=b'', to='master.CategoriaCliente', null=True),
            preserve_default=True,
        ),
    ]
