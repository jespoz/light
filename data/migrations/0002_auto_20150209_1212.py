# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='formulaingreso',
            options={},
        ),
        migrations.RemoveField(
            model_name='formulaingreso',
            name='cadena',
        ),
        migrations.RemoveField(
            model_name='formulaingreso',
            name='categoriaCliente',
        ),
        migrations.RemoveField(
            model_name='formulaingreso',
            name='clienteLocal',
        ),
        migrations.RemoveField(
            model_name='formulaingreso',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='formulaingreso',
            name='kilos',
        ),
        migrations.RemoveField(
            model_name='formulaingreso',
            name='mes',
        ),
        migrations.RemoveField(
            model_name='formulaingreso',
            name='netos',
        ),
        migrations.RemoveField(
            model_name='formulaingreso',
            name='sector',
        ),
        migrations.RemoveField(
            model_name='formulaingreso',
            name='subcadena',
        ),
        migrations.RemoveField(
            model_name='formulaingreso',
            name='tipoCliente',
        ),
        migrations.RemoveField(
            model_name='formulaingreso',
            name='year',
        ),
        migrations.RemoveField(
            model_name='formulaingreso',
            name='zonaVentas',
        ),
    ]
