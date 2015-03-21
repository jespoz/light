# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financials', '0045_costoventa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='costoventa',
            name='claseCoste',
        ),
        migrations.RemoveField(
            model_name='costoventa',
            name='oficina',
        ),
        migrations.RemoveField(
            model_name='costoventa',
            name='periodo',
        ),
        migrations.DeleteModel(
            name='CostoVenta',
        ),
    ]
