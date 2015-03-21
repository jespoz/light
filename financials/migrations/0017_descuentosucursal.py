# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0007_cadena'),
        ('financials', '0016_descuentocomercial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DescuentoSucursal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vigente', models.FloatField(default=0)),
                ('pedido', models.FloatField(default=0)),
                ('facturado', models.FloatField(default=0)),
                ('oficina', models.ForeignKey(to='master.OficinaVentas')),
                ('periodo', models.ForeignKey(to='master.Periodo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
