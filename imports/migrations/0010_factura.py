# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0028_localesnulos'),
        ('imports', '0009_ventacompleta_referencia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('referencia', models.IntegerField(default=0)),
                ('codigoMaterial', models.IntegerField()),
                ('vigente', models.FloatField(default=0)),
                ('pedido', models.FloatField(default=0)),
                ('facturado', models.FloatField(default=0)),
                ('periodo', models.ForeignKey(to='master.Periodo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
