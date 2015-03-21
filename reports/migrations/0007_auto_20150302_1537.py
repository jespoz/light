# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0006_infografia_periodo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='infografia',
            old_name='periodo',
            new_name='tipoPeriodo',
        ),
    ]
