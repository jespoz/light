# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0007_cadena'),
    ]

    operations = [
        migrations.CreateModel(
            name='CCNivel1',
            fields=[
                ('codigo', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('clasecoste', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CCNivel2',
            fields=[
                ('codigo', models.CharField(max_length=20, serialize=False, primary_key=True)),
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
                ('codigo', models.CharField(max_length=20, serialize=False, primary_key=True)),
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
                ('codigo', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('clasecoste', models.CharField(max_length=200)),
                ('nivel3', models.ForeignKey(to='master.CCNivel3')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='clasescoste',
            old_name='clasecoste4',
            new_name='clasecoste',
        ),
    ]
