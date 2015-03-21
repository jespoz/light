# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0015_ccnivel2_seudo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClasePedido',
            fields=[
                ('codigo', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('clase', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
