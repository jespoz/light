# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0026_cliente_sector'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClienteInterlocutor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cliente', models.IntegerField(max_length=20)),
                ('supervisor', models.CharField(default=b'', max_length=200, null=True, blank=True)),
                ('preventa', models.CharField(default=b'', max_length=200, null=True, blank=True)),
                ('sector', models.ForeignKey(default=b'', blank=True, to='master.Sector', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='preventa',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='sector',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='supervisor',
        ),
    ]
