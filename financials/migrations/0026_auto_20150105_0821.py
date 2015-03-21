# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0015_ccnivel2_seudo'),
        ('financials', '0025_costomerchandising'),
    ]

    operations = [
        migrations.CreateModel(
            name='CostoApertura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('costo', models.FloatField(default=0)),
                ('claseCoste', models.ForeignKey(to='master.ClasesCoste')),
                ('oficina', models.ForeignKey(to='master.OficinaVentas')),
                ('periodo', models.ForeignKey(to='master.Periodo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='costomerchandising',
            name='claseCoste',
        ),
        migrations.RemoveField(
            model_name='costomerchandising',
            name='oficina',
        ),
        migrations.RemoveField(
            model_name='costomerchandising',
            name='periodo',
        ),
        migrations.DeleteModel(
            name='CostoMerchandising',
        ),
    ]
