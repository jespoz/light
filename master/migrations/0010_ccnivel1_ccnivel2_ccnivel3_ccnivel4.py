# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0009_auto_20150103_1610'),
    ]

    operations = [
        migrations.CreateModel(
            name='CCNivel1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clasecoste', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CCNivel2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clasecoste', models.CharField(max_length=200)),
                ('nivel1', models.ForeignKey(to='master.CCNivel1')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CCNivel3',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clasecoste', models.CharField(max_length=200)),
                ('nivel2', models.ForeignKey(to='master.CCNivel2')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CCNivel4',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clasecoste', models.CharField(max_length=200)),
                ('nivel3', models.ForeignKey(to='master.CCNivel3')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
