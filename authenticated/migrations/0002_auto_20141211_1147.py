# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authenticated', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('canal', models.ManyToManyField(to='authenticated.Canal')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='canal',
            options={'verbose_name_plural': 'Canales'},
        ),
        migrations.AlterField(
            model_name='cadena',
            name='icono',
            field=models.ImageField(upload_to=b'/iconos/', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='canal',
            name='icono',
            field=models.ImageField(upload_to=b'/iconos/', blank=True),
            preserve_default=True,
        ),
    ]
