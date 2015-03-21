# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0028_localesnulos'),
        ('actions', '0006_auto_20150319_1027'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dispersion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('responsable', models.CharField(max_length=100)),
                ('negocio', models.CharField(max_length=100)),
                ('unidad', models.IntegerField(default=0)),
                ('diferencia', models.FloatField(default=0)),
                ('oficina', models.ForeignKey(to='master.OficinaVentas')),
                ('periodo', models.ForeignKey(to='master.Periodo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
