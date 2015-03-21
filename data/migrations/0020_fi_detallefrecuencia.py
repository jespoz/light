# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0024_sector_grupo'),
        ('data', '0019_formuladeingreso_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='FI_DetalleFrecuencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('frecuencia', models.FloatField(default=0)),
                ('categoria', models.ForeignKey(to='master.CategoriaCliente')),
                ('grupo', models.ForeignKey(to='master.GrupoSector')),
                ('oficina', models.ForeignKey(to='master.OficinaVentas')),
                ('periodo', models.ForeignKey(to='master.Periodo')),
                ('tipoCliente', models.ForeignKey(to='master.TipoCliente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
