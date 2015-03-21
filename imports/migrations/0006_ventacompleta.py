# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0028_localesnulos'),
        ('imports', '0005_timeline'),
    ]

    operations = [
        migrations.CreateModel(
            name='VentaCompleta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cliente', models.IntegerField(max_length=20)),
                ('fecha', models.DateField()),
                ('supervisor', models.CharField(default=b'', max_length=200, null=True, blank=True)),
                ('preventa', models.CharField(default=b'', max_length=200, null=True, blank=True)),
                ('codigoMaterial', models.IntegerField()),
                ('material', models.CharField(max_length=100)),
                ('nivel2', models.CharField(max_length=100)),
                ('nivel3', models.CharField(max_length=100)),
                ('marca', models.CharField(max_length=100)),
                ('kilo', models.FloatField(default=0)),
                ('neto', models.FloatField(default=0)),
                ('categoria', models.ForeignKey(to='master.CategoriaCliente')),
                ('oficina', models.ForeignKey(to='master.OficinaVentas')),
                ('sector', models.ForeignKey(to='master.Sector')),
                ('tipoCliente', models.ForeignKey(to='master.TipoCliente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
