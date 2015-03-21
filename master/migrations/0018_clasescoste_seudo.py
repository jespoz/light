# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0017_tipocliente_abreviacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='clasescoste',
            name='seudo',
            field=models.CharField(default=b'', max_length=100, null=True),
            preserve_default=True,
        ),
    ]
