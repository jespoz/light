# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0020_ccnivel3_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('codigo', models.IntegerField(max_length=20, serialize=False, primary_key=True)),
                ('cliente', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('poblacion', models.CharField(max_length=100, null=True)),
                ('creacion', models.DateField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
