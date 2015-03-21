# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0021_cliente'),
        ('data', '0013_fi_locales_fi_localesfugados_fi_localesnuevos_fi_localesrecuperados'),
    ]

    operations = [
        migrations.CreateModel(
            name='IconosLocales',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fa_locales', models.IntegerField(default=0)),
                ('fa_nuevos', models.IntegerField(default=0)),
                ('fa_recuperados', models.IntegerField(default=0)),
                ('oficina', models.ForeignKey(to='master.OficinaVentas')),
                ('periodo', models.ForeignKey(to='master.Periodo')),
                ('tipoCliente', models.ForeignKey(to='master.TipoCliente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
