# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0017_tipocliente_abreviacion'),
        ('financials', '0032_descuentovigente'),
    ]

    operations = [
        migrations.CreateModel(
            name='DescuentoPedido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descuento', models.FloatField(default=0)),
                ('oficina', models.ForeignKey(to='master.OficinaVentas')),
                ('periodo', models.ForeignKey(to='master.Periodo')),
                ('tipoCliente', models.ForeignKey(to='master.TipoCliente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='descuentotipo',
            name='oficina',
        ),
        migrations.RemoveField(
            model_name='descuentotipo',
            name='periodo',
        ),
        migrations.RemoveField(
            model_name='descuentotipo',
            name='tipoCliente',
        ),
        migrations.DeleteModel(
            name='DescuentoTipo',
        ),
    ]
