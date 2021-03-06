# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0007_auto_20150302_1537'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('master', '0024_sector_grupo'),
        ('imports', '0002_auto_20150128_0210'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistorialCreacionReporte',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('actualizacion', models.DateTimeField(auto_now_add=True)),
                ('periodo', models.ForeignKey(to='master.Periodo')),
                ('reporte', models.ForeignKey(to='reports.Reporte')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
