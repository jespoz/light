# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0006_tipocliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cadena',
            fields=[
                ('codigo', models.CharField(max_length=2, serialize=False, primary_key=True)),
                ('cadena', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
