# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0006_infografia_periodo'),
        ('master', '0024_sector_grupo'),
        ('random_messages', '0003_mensajesaleatorios'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hash', models.CharField(max_length=100)),
                ('valor', models.TextField()),
                ('oficina', models.ForeignKey(to='master.OficinaVentas')),
                ('periodo', models.ForeignKey(to='master.Periodo')),
                ('reporte', models.ForeignKey(to='reports.Reporte')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
