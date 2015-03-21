# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0017_tipocliente_abreviacion'),
        ('financials', '0039_auto_20150119_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='PesoDescCallPed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total', models.FloatField(default=0)),
                ('call', models.FloatField(default=0)),
                ('oficina', models.ForeignKey(to='master.OficinaVentas')),
                ('periodo', models.ForeignKey(to='master.Periodo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='pesodescuentocall',
            name='oficina',
        ),
        migrations.RemoveField(
            model_name='pesodescuentocall',
            name='periodo',
        ),
        migrations.DeleteModel(
            name='PesoDescuentoCall',
        ),
    ]
