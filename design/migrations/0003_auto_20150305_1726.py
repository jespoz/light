# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authenticated', '0006_accesoreporte'),
        ('design', '0002_auto_20150304_0959'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acceso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cargo', models.ForeignKey(to='authenticated.Cargo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Navegacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nav', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='acceso',
            name='navegacion',
            field=models.ForeignKey(to='design.Navegacion'),
            preserve_default=True,
        ),
    ]
