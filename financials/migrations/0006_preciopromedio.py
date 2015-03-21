# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0004_auto_20141230_1420'),
        ('financials', '0005_auto_20141230_1351'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrecioPromedio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('aa', models.FloatField(default=0)),
                ('ac', models.FloatField(default=0)),
                ('oficina', models.ForeignKey(to='master.OficinaVentas')),
                ('periodo', models.ForeignKey(to='master.Periodo')),
                ('sector', models.ForeignKey(to='master.Sector')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
