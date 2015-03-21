# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0024_sector_grupo'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccLocal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codLocal', models.CharField(max_length=20)),
                ('clienteLocal', models.CharField(max_length=200)),
                ('promedio', models.FloatField(default=0)),
                ('desviacion', models.FloatField(default=0)),
                ('minimo', models.IntegerField(default=0)),
                ('maximo', models.IntegerField(default=0)),
                ('ventaPromedio', models.FloatField(default=0)),
                ('semCalculo', models.IntegerField(default=0)),
                ('categoria', models.ForeignKey(to='master.CategoriaCliente')),
                ('oficina', models.ForeignKey(to='master.OficinaVentas')),
                ('periodo', models.ForeignKey(to='master.Periodo')),
                ('tipoCliente', models.ForeignKey(to='master.TipoCliente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
