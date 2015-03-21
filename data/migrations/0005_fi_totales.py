# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0019_periodo_tipoperiodo'),
        ('data', '0004_formuladeingreso'),
    ]

    operations = [
        migrations.CreateModel(
            name='FI_Totales',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kilo', models.FloatField()),
                ('neto', models.FloatField()),
                ('precio', models.FloatField()),
                ('locales', models.FloatField()),
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
