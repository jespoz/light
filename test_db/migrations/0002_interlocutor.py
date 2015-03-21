# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_db', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interlocutor',
            fields=[
                ('codigo', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
