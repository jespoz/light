# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0019_periodo_tipoperiodo'),
        ('data', '0003_delete_formulaingreso'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormulaDeIngreso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cliente', models.CharField(max_length=20)),
                ('fecha', models.DateField()),
                ('kilo', models.FloatField()),
                ('neto', models.FloatField()),
                ('oficina', models.ForeignKey(to='master.OficinaVentas')),
                ('periodo', models.ForeignKey(to='master.Periodo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
