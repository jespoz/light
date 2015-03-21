# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0018_clasescoste_seudo'),
        ('financials', '0047_costoapertura_peso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unitario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ingreso', models.FloatField(default=0)),
                ('gasto', models.FloatField(default=0)),
                ('oficina', models.ForeignKey(to='master.OficinaVentas')),
                ('periodo', models.ForeignKey(to='master.Periodo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
