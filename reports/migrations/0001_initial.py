# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Infografia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('infografia', models.CharField(max_length=100)),
                ('descripcion', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reporte', models.CharField(max_length=100)),
                ('descripcion', models.TextField(null=True, blank=True)),
                ('infografia', models.ForeignKey(to='reports.Infografia')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
