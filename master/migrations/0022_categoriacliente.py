# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0021_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaCliente',
            fields=[
                ('codigo', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('categoria', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
