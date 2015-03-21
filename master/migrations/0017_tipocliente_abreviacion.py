# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0016_clasepedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipocliente',
            name='abreviacion',
            field=models.CharField(default=b'', max_length=10),
            preserve_default=True,
        ),
    ]
