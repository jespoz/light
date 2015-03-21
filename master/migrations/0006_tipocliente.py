# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0005_sector_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoCliente',
            fields=[
                ('codigo', models.CharField(max_length=2, serialize=False, primary_key=True)),
                ('tipo', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Tipo de Cliente',
                'verbose_name_plural': 'Tipos de Clientes',
            },
            bases=(models.Model,),
        ),
    ]
