# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0004_auto_20141230_1420'),
        ('financials', '0007_auto_20141230_1701'),
    ]

    operations = [
        migrations.CreateModel(
            name='PPOficina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('precio', models.FloatField(default=0)),
                ('oficina', models.ForeignKey(to='master.OficinaVentas')),
                ('periodo', models.ForeignKey(to='master.Periodo')),
                ('sector', models.ForeignKey(to='master.Sector')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
