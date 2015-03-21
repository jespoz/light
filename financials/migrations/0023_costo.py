# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0014_auto_20150104_2017'),
        ('financials', '0022_auto_20150103_1637'),
    ]

    operations = [
        migrations.CreateModel(
            name='Costo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('costo', models.FloatField(default=0)),
                ('claseCoste', models.ForeignKey(to='master.CCNivel2')),
                ('oficina', models.ForeignKey(to='master.OficinaVentas')),
                ('periodo', models.ForeignKey(to='master.Periodo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
