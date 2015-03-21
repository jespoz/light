# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authenticated', '0006_accesoreporte'),
        ('design', '0004_auto_20150305_1734'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acceso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cargo', models.ForeignKey(to='authenticated.Cargo')),
                ('navegacion', models.ManyToManyField(to='design.Navegacion')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
