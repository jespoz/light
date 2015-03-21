# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0028_localesnulos'),
        ('actions', '0004_analisisdescuentototales'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnalisisDescuentoApertura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('supervisor', models.CharField(default=b'', max_length=200, null=True, blank=True)),
                ('preventa', models.CharField(default=b'', max_length=200, null=True, blank=True)),
                ('codLocal', models.CharField(max_length=20)),
                ('clienteLocal', models.CharField(max_length=200)),
                ('codigoMaterial', models.IntegerField()),
                ('material', models.CharField(max_length=100)),
                ('negocio', models.CharField(max_length=100)),
                ('responsable', models.CharField(max_length=100)),
                ('uno', models.FloatField(default=0)),
                ('dos', models.FloatField(default=0)),
                ('trs', models.FloatField(default=0)),
                ('cuatro', models.FloatField(default=0)),
                ('cinco', models.FloatField(default=0)),
                ('seisAdiez', models.FloatField(default=0)),
                ('onceAveinte', models.FloatField(default=0)),
                ('mayorVeinte', models.FloatField(default=0)),
                ('categoria', models.ForeignKey(to='master.CategoriaCliente')),
                ('oficina', models.ForeignKey(to='master.OficinaVentas')),
                ('periodo', models.ForeignKey(to='master.Periodo')),
                ('sector', models.ForeignKey(to='master.Sector')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
