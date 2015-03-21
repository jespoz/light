# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0006_infografia_periodo'),
        ('random_messages', '0002_auto_20150225_1454'),
    ]

    operations = [
        migrations.CreateModel(
            name='MensajesAleatorios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.IntegerField(default=0)),
                ('primera_titulo', models.CharField(max_length=30)),
                ('primera_mensaje', models.TextField()),
                ('segunda_titulo', models.CharField(max_length=30)),
                ('segunda_mensaje', models.TextField()),
                ('tercera_titulo', models.CharField(max_length=30)),
                ('tercera_mensaje', models.TextField()),
                ('reporte', models.ForeignKey(to='reports.Reporte')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
