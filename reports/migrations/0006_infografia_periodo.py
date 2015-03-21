# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0005_remove_infografia_periodo'),
    ]

    operations = [
        migrations.AddField(
            model_name='infografia',
            name='periodo',
            field=models.ForeignKey(default=b'', to='reports.TipoPeriodo', null=True),
            preserve_default=True,
        ),
    ]
