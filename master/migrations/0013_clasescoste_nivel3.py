# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0012_auto_20150104_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='clasescoste',
            name='nivel3',
            field=models.ForeignKey(default=b'', to='master.CCNivel3', null=True),
            preserve_default=True,
        ),
    ]
