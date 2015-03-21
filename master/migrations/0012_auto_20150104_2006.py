# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0011_auto_20150103_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clasescoste',
            name='clasecoste1',
        ),
        migrations.RemoveField(
            model_name='clasescoste',
            name='clasecoste2',
        ),
        migrations.RemoveField(
            model_name='clasescoste',
            name='clasecoste3',
        ),
    ]
