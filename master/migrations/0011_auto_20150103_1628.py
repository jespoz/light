# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0010_ccnivel1_ccnivel2_ccnivel3_ccnivel4'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ccnivel4',
            name='id',
        ),
        migrations.AddField(
            model_name='ccnivel4',
            name='codigo',
            field=models.CharField(default=b'', max_length=20, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
