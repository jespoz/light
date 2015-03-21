# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0006_tipocliente'),
        ('financials', '0012_auto_20141231_1235'),
    ]

    operations = [
        migrations.CreateModel(
            name='PPTipoClienteSector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('precio', models.FloatField(default=0)),
                ('variacion', models.FloatField(default=0)),
                ('oficina', models.ForeignKey(to='master.OficinaVentas')),
                ('periodo', models.ForeignKey(to='master.Periodo')),
                ('sector', models.ForeignKey(to='master.Sector')),
                ('tipoCliente', models.ForeignKey(to='master.TipoCliente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
