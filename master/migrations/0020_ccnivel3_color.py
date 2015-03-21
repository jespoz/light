# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0019_periodo_tipoperiodo'),
    ]

    operations = [
        migrations.AddField(
            model_name='ccnivel3',
            name='color',
            field=models.CharField(default=b'', max_length=10, null=True),
            preserve_default=True,
        ),
    ]
