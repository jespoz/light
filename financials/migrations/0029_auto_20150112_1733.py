# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0015_ccnivel2_seudo'),
        ('financials', '0028_auto_20150112_1336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kilos',
            name='sector',
        ),
        migrations.AddField(
            model_name='kilos',
            name='tipoCliente',
            field=models.ForeignKey(default=b'', to='master.TipoCliente', null=True),
            preserve_default=True,
        ),
    ]
