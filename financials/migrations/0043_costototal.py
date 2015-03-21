# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0017_tipocliente_abreviacion'),
        ('financials', '0042_auto_20150119_1840'),
    ]

    operations = [
        migrations.CreateModel(
            name='CostoTotal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sucursal', models.FloatField(default=0)),
                ('zonal', models.FloatField(default=0)),
                ('nacional', models.FloatField(default=0)),
                ('oficina', models.ForeignKey(to='master.OficinaVentas')),
                ('periodo', models.ForeignKey(to='master.Periodo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
