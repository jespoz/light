# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0021_cliente'),
        ('data', '0015_auto_20150223_0019'),
    ]

    operations = [
        migrations.CreateModel(
            name='FI_MesAnterior',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('precio', models.FloatField()),
                ('local', models.FloatField()),
                ('frecuencia', models.FloatField()),
                ('ticket', models.FloatField()),
                ('oficina', models.ForeignKey(to='master.OficinaVentas')),
                ('periodo', models.ForeignKey(to='master.Periodo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
