# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authenticated', '0002_auto_20141211_1147'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='perfil',
            options={'verbose_name_plural': 'Perfiles'},
        ),
        migrations.AddField(
            model_name='perfil',
            name='cadena',
            field=models.ManyToManyField(to='authenticated.Cadena'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='perfil',
            name='oficina',
            field=models.ManyToManyField(to='authenticated.Oficina'),
            preserve_default=True,
        ),
    ]
