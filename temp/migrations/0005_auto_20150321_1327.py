# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('temp', '0004_tablafinalaccpreciototal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tablafinalaccpreciototal',
            name='oficina',
        ),
        migrations.RemoveField(
            model_name='tablafinalaccpreciototal',
            name='periodo',
        ),
        migrations.RemoveField(
            model_name='tablafinalaccpreciototal',
            name='sector',
        ),
        migrations.DeleteModel(
            name='TablaFinalAccPrecioTotal',
        ),
    ]
