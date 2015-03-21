# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0023_gruposector'),
    ]

    operations = [
        migrations.AddField(
            model_name='sector',
            name='grupo',
            field=models.ForeignKey(default=b'', to='master.GrupoSector', null=True),
            preserve_default=True,
        ),
    ]
