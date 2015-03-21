# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financials', '0021_descuentosector'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gasto',
            name='clasecoste',
            field=models.ForeignKey(to='master.ClasesCoste'),
            preserve_default=True,
        ),
    ]
