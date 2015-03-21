# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0004_auto_20150202_1901'),
        ('master', '0018_clasescoste_seudo'),
    ]

    operations = [
        migrations.AddField(
            model_name='periodo',
            name='tipoPeriodo',
            field=models.ForeignKey(default=b'', to='reports.TipoPeriodo', null=True),
            preserve_default=True,
        ),
    ]
