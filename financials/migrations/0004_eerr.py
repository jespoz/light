# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0002_sector'),
        ('financials', '0003_kilos_sector'),
    ]

    operations = [
        migrations.CreateModel(
            name='EERR',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kilo', models.FloatField(default=0, null=True)),
                ('venta', models.FloatField(default=0, null=True)),
                ('ingreso', models.FloatField(default=0, null=True)),
                ('gasto', models.FloatField(default=0, null=True)),
                ('margen_peso', models.FloatField(default=0, null=True)),
                ('margen_porc', models.FloatField(default=0, null=True)),
                ('oficina', models.ForeignKey(to='master.OficinaVentas')),
                ('periodo', models.ForeignKey(to='master.Periodo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
