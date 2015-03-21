# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Indicador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('indicador', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Visualizacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('resultado', models.FloatField(default=0)),
                ('actualizacion', models.DateTimeField(auto_now_add=True)),
                ('periodo', models.CharField(max_length=20)),
                ('visualizacion', models.IntegerField(default=0)),
                ('analista', models.ForeignKey(related_name='analista', to=settings.AUTH_USER_MODEL)),
                ('indicador', models.ForeignKey(to='indicators.Indicador')),
                ('usuario', models.ForeignKey(related_name='usuario', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
