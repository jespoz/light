# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0028_localesnulos'),
        ('imports', '0006_ventacompleta'),
    ]

    operations = [
        migrations.AddField(
            model_name='ventacompleta',
            name='periodo',
            field=models.ForeignKey(default=b'', to='master.Periodo'),
            preserve_default=True,
        ),
    ]
