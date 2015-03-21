# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0004_auto_20141230_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='sector',
            name='id',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
