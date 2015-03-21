# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0002_sector'),
        ('financials', '0004_eerr'),
    ]

    operations = [
        migrations.CreateModel(
            name='MargenMensual',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('aa', models.FloatField(default=0)),
                ('ac', models.FloatField(default=0)),
                ('oficina', models.ForeignKey(to='master.OficinaVentas')),
                ('periodo', models.ForeignKey(to='master.Periodo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='eerr',
            options={'verbose_name': 'Estado de Resultado', 'verbose_name_plural': 'Estados de Resultado'},
        ),
    ]
