# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0015_ccnivel2_seudo'),
        ('financials', '0027_estadoresultado'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadosResultados',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kilo', models.FloatField(default=0, null=True)),
                ('venta', models.FloatField(default=0, null=True)),
                ('ingreso', models.FloatField(default=0, null=True)),
                ('gasto', models.FloatField(default=0, null=True)),
                ('margen_peso', models.FloatField(default=0, null=True)),
                ('margen_porc', models.FloatField(default=0, null=True)),
                ('crec_kilo', models.FloatField(default=0, null=True)),
                ('crec_venta', models.FloatField(default=0, null=True)),
                ('crec_ingreso', models.FloatField(default=0, null=True)),
                ('crec_gasto', models.FloatField(default=0, null=True)),
                ('oficina', models.ForeignKey(to='master.OficinaVentas')),
                ('periodo', models.ForeignKey(to='master.Periodo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='estadoresultado',
            name='oficina',
        ),
        migrations.RemoveField(
            model_name='estadoresultado',
            name='periodo',
        ),
        migrations.DeleteModel(
            name='EstadoResultado',
        ),
    ]
