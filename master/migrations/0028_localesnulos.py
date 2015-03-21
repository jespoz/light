# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0027_auto_20150317_0905'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocalesNulos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cliente', models.IntegerField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
