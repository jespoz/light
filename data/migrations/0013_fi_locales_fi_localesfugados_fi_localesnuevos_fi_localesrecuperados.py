# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0021_cliente'),
        ('data', '0012_fi_detalleprecio'),
    ]

    operations = [
        migrations.CreateModel(
            name='FI_Locales',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('locales', models.IntegerField(default=0)),
                ('oficina', models.ForeignKey(to='master.OficinaVentas')),
                ('periodo', models.ForeignKey(to='master.Periodo')),
                ('tipoCliente', models.ForeignKey(to='master.TipoCliente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FI_LocalesFugados',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('locales', models.IntegerField(default=0)),
                ('oficina', models.ForeignKey(to='master.OficinaVentas')),
                ('periodo', models.ForeignKey(to='master.Periodo')),
                ('tipoCliente', models.ForeignKey(to='master.TipoCliente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FI_LocalesNuevos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('locales', models.IntegerField(default=0)),
                ('oficina', models.ForeignKey(to='master.OficinaVentas')),
                ('periodo', models.ForeignKey(to='master.Periodo')),
                ('tipoCliente', models.ForeignKey(to='master.TipoCliente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FI_LocalesRecuperados',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('locales', models.IntegerField(default=0)),
                ('oficina', models.ForeignKey(to='master.OficinaVentas')),
                ('periodo', models.ForeignKey(to='master.Periodo')),
                ('tipoCliente', models.ForeignKey(to='master.TipoCliente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
