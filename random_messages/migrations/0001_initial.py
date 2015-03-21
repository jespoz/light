# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0006_infografia_periodo'),
        ('master', '0024_sector_grupo'),
    ]

    operations = [
        migrations.CreateModel(
            name='MensajeReporte',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('primera', models.IntegerField(default=0)),
                ('segunda', models.IntegerField(default=0)),
                ('tercera', models.IntegerField(default=0)),
                ('oficina', models.ForeignKey(to='master.OficinaVentas')),
                ('periodo', models.ForeignKey(to='master.Periodo')),
                ('reporte', models.ForeignKey(to='reports.Reporte')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
