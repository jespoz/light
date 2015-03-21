# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0002_sector'),
        ('financials', '0002_gasto'),
    ]

    operations = [
        migrations.AddField(
            model_name='kilos',
            name='sector',
            field=models.ForeignKey(default=b'', to='master.Sector', null=True),
            preserve_default=True,
        ),
    ]
