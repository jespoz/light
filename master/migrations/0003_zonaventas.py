# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0002_sector'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZonaVentas',
            fields=[
                ('codigo', models.CharField(max_length=4, serialize=False, primary_key=True)),
                ('zona', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
