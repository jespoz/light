# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financials', '0006_preciopromedio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='preciopromedio',
            old_name='aa',
            new_name='kilo',
        ),
        migrations.RenameField(
            model_name='preciopromedio',
            old_name='ac',
            new_name='neto',
        ),
    ]
