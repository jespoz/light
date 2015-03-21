# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClasesCoste',
            fields=[
                ('codigo', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('clasecoste4', models.CharField(max_length=200)),
                ('clasecoste3', models.CharField(max_length=200)),
                ('clasecoste2', models.CharField(max_length=200)),
                ('clasecoste1', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OficinaVentas',
            fields=[
                ('codigo', models.CharField(max_length=4, serialize=False, primary_key=True)),
                ('oficina', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Oficina de Ventas',
                'verbose_name_plural': 'Oficinas de Ventas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('periodo', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
