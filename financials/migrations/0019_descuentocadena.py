# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0007_cadena'),
        ('financials', '0018_descuentotipo'),
    ]

    operations = [
        migrations.CreateModel(
            name='DescuentoCadena',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descuento', models.FloatField(default=0)),
                ('cadena', models.ForeignKey(to='master.Cadena')),
                ('oficina', models.ForeignKey(to='master.OficinaVentas')),
                ('periodo', models.ForeignKey(to='master.Periodo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
