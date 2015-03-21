# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('random_messages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensajereporte',
            name='primera',
            field=models.IntegerField(default=0, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mensajereporte',
            name='segunda',
            field=models.IntegerField(default=0, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mensajereporte',
            name='tercera',
            field=models.IntegerField(default=0, null=True),
            preserve_default=True,
        ),
    ]
