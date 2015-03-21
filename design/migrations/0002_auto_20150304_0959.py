# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datostimeline',
            name='oficina',
            field=models.ForeignKey(to='master.OficinaVentas'),
            preserve_default=True,
        ),
    ]
