# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0008_reporte_icono'),
        ('authenticated', '0006_accesoreporte'),
        ('master', '0024_sector_grupo'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatosTimeline',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('resultado', models.FloatField(default=0)),
                ('oficina', models.ForeignKey(to='authenticated.Oficina')),
                ('periodo', models.ForeignKey(to='master.Periodo')),
                ('reporte', models.ForeignKey(to='reports.Reporte')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
