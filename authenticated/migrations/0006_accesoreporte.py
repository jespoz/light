# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0007_auto_20150302_1537'),
        ('authenticated', '0005_perfil_cargo'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccesoReporte',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cargo', models.ForeignKey(to='authenticated.Cargo')),
                ('reporte', models.ManyToManyField(to='reports.Reporte')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
