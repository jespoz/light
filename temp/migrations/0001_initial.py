# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0028_localesnulos'),
    ]

    operations = [
        migrations.CreateModel(
            name='VentaSumatoriaMaterial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigoMaterial', models.IntegerField()),
                ('neto', models.FloatField(default=0)),
                ('sumatoria', models.FloatField(default=0)),
                ('oficina', models.ForeignKey(to='master.OficinaVentas')),
                ('periodo', models.ForeignKey(to='master.Periodo')),
                ('tipoCliente', models.ForeignKey(to='master.TipoCliente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
