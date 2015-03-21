# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0015_ccnivel2_seudo'),
        ('financials', '0023_costo'),
    ]

    operations = [
        migrations.CreateModel(
            name='CostoVentas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('costo', models.FloatField(default=0)),
                ('claseCoste', models.ForeignKey(to='master.CCNivel3')),
                ('oficina', models.ForeignKey(to='master.OficinaVentas')),
                ('periodo', models.ForeignKey(to='master.Periodo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
