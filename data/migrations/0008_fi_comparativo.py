# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0019_periodo_tipoperiodo'),
        ('data', '0007_auto_20150216_0921'),
    ]

    operations = [
        migrations.CreateModel(
            name='FI_Comparativo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sem_precio', models.FloatField()),
                ('mes_precio', models.FloatField()),
                ('sem_local', models.FloatField()),
                ('mes_local', models.FloatField()),
                ('sem_frecuencia', models.FloatField()),
                ('mes_frecuencia', models.FloatField()),
                ('sem_ticket', models.FloatField()),
                ('mes_ticket', models.FloatField()),
                ('oficina', models.ForeignKey(to='master.OficinaVentas')),
                ('periodo', models.ForeignKey(to='master.Periodo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
