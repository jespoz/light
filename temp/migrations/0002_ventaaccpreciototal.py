# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0028_localesnulos'),
        ('temp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VentaAccPrecioTotal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('referencia', models.IntegerField(default=0)),
                ('unidad', models.FloatField(default=0)),
                ('codigoMaterial', models.IntegerField()),
                ('material', models.CharField(max_length=100)),
                ('oficina', models.ForeignKey(to='master.OficinaVentas')),
                ('periodo', models.ForeignKey(to='master.Periodo')),
                ('sector', models.ForeignKey(to='master.Sector')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
