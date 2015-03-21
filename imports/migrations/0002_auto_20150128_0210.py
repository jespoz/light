# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imports.models


class Migration(migrations.Migration):

    dependencies = [
        ('imports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='archivo',
            field=models.FileField(upload_to=imports.models.get_upload_file_name),
            preserve_default=True,
        ),
    ]
