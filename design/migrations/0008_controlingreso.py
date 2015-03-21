# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0011_remove_reporte_nav'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('design', '0007_auto_20150309_1036'),
    ]

    operations = [
        migrations.CreateModel(
            name='ControlIngreso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ingreso', models.DateTimeField()),
                ('salida', models.DateTimeField(null=True)),
                ('reporte', models.ForeignKey(to='reports.Reporte')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
