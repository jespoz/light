# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormulaIngreso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('oficinaVentas', models.CharField(max_length=100)),
                ('tipoCliente', models.CharField(max_length=100)),
                ('categoriaCliente', models.CharField(max_length=100)),
                ('sector', models.CharField(max_length=100)),
                ('clienteLocal', models.CharField(default=b'', max_length=100)),
                ('zonaVentas', models.CharField(max_length=100)),
                ('mes', models.IntegerField(default=0)),
                ('year', models.IntegerField(default=0)),
                ('cadena', models.CharField(max_length=100)),
                ('subcadena', models.CharField(max_length=100)),
                ('fecha', models.DateField(null=True)),
                ('netos', models.FloatField(default=0)),
                ('kilos', models.FloatField(default=0)),
            ],
            options={
                'verbose_name': 'Formula de Ingreso',
                'verbose_name_plural': 'Formula de Ingreso',
            },
            bases=(models.Model,),
        ),
    ]
