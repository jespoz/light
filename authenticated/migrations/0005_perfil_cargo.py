# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authenticated', '0004_cargo'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='cargo',
            field=models.ForeignKey(default=b'', to='authenticated.Cargo'),
            preserve_default=True,
        ),
    ]
