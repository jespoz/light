# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0007_cadena'),
        ('financials', '0013_pptipoclientesector'),
    ]

    operations = [
        migrations.CreateModel(
            name='Descuento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kilo', models.FloatField(default=0)),
                ('base', models.FloatField(default=0)),
                ('especial', models.FloatField(default=0)),
                ('vigente', models.FloatField(default=0)),
                ('pedido', models.FloatField(default=0)),
                ('facturado', models.FloatField(default=0)),
                ('cadena', models.ForeignKey(to='master.Cadena')),
                ('oficina', models.ForeignKey(to='master.OficinaVentas')),
                ('periodo', models.ForeignKey(to='master.Periodo')),
                ('tipoCliente', models.ForeignKey(to='master.TipoCliente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
