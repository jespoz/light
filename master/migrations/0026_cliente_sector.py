# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0025_auto_20150316_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='sector',
            field=models.ForeignKey(default=b'', blank=True, to='master.Sector', null=True),
            preserve_default=True,
        ),
    ]
