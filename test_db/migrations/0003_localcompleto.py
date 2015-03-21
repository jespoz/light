# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0026_cliente_sector'),
        ('test_db', '0002_interlocutor'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocalCompleto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cliente', models.CharField(max_length=100)),
                ('preventa', models.CharField(max_length=200)),
                ('supervisor', models.CharField(max_length=200)),
                ('sector', models.ForeignKey(to='master.Sector')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
