# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0007_cadena'),
        ('financials', '0014_descuento'),
    ]

    operations = [
        migrations.CreateModel(
            name='DescuentoTotal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descuento', models.FloatField(default=0)),
                ('comercial', models.FloatField(default=0)),
                ('sucursal', models.FloatField(default=0)),
                ('participacion', models.FloatField(default=0)),
                ('oficina', models.ForeignKey(to='master.OficinaVentas')),
                ('periodo', models.ForeignKey(to='master.Periodo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
