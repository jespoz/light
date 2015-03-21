# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_reporte_matriz'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoPeriodo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=140)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='infografia',
            name='periodo',
            field=models.ForeignKey(default=b'', to='reports.TipoPeriodo', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reporte',
            name='matriz',
            field=models.FileField(null=True, upload_to=b'matrices/', blank=True),
            preserve_default=True,
        ),
    ]
