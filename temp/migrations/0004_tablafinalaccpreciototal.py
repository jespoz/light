# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0028_localesnulos'),
        ('temp', '0003_baseaccpreciototal'),
    ]

    operations = [
        migrations.CreateModel(
            name='TablaFinalAccPrecioTotal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigoMaterial', models.IntegerField()),
                ('material', models.CharField(max_length=100)),
                ('con', models.FloatField(default=0)),
                ('sin', models.FloatField(default=0)),
                ('sobre', models.FloatField(default=0)),
                ('oficina', models.ForeignKey(to='master.OficinaVentas')),
                ('periodo', models.ForeignKey(to='master.Periodo')),
                ('sector', models.ForeignKey(to='master.Sector')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
