# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('codigo', models.CharField(max_length=2, serialize=False, primary_key=True)),
                ('sector', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Sectores',
            },
            bases=(models.Model,),
        ),
    ]
