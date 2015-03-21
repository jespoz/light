# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financials', '0052_auto_20150224_1229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='descuento',
            name='cliente',
        ),
    ]
