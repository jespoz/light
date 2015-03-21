# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0019_periodo_tipoperiodo'),
        ('data', '0010_auto_20150217_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='formuladeingreso',
            name='sector',
            field=models.ForeignKey(default=b'', to='master.Sector', null=True),
            preserve_default=True,
        ),
    ]
