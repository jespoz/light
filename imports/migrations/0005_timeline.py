# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0007_auto_20150302_1537'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('master', '0024_sector_grupo'),
        ('imports', '0004_auto_20150302_1603'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timeline',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('actualizacion', models.DateTimeField()),
                ('creado_por', models.ForeignKey(related_name='creador', to=settings.AUTH_USER_MODEL)),
                ('periodo', models.ForeignKey(to='master.Periodo')),
                ('reporte', models.ForeignKey(to='reports.Reporte')),
                ('usuario', models.ForeignKey(related_name='usuario_lector', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
