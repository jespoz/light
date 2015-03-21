# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0028_localesnulos'),
        ('actions', '0003_acclocal_sector'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnalisisDescuentoTotales',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigoMaterial', models.IntegerField()),
                ('material', models.CharField(max_length=100)),
                ('conDescuento', models.IntegerField()),
                ('sinDescuento', models.IntegerField()),
                ('sobreprecio', models.IntegerField()),
                ('oficina', models.ForeignKey(to='master.OficinaVentas')),
                ('periodo', models.ForeignKey(to='master.Periodo')),
                ('sector', models.ForeignKey(to='master.Sector')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
