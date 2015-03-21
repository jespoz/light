# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0026_cliente_sector'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocalSector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cliente', models.CharField(max_length=100)),
                ('funcionario', models.CharField(max_length=50)),
                ('interlocutor', models.CharField(max_length=50)),
                ('sector', models.ForeignKey(to='master.Sector')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
