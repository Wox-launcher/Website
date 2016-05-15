# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import plugins.models


class Migration(migrations.Migration):

    dependencies = [
        ('plugins', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plugin',
            name='icon',
            field=models.ImageField(help_text='Only support .jpg and .png image', upload_to=plugins.models.get_file_path, max_length=500, verbose_name='Plugin Icon'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='plugin',
            name='preview',
            field=models.ImageField(max_length=500, upload_to=plugins.models.get_file_path, null=True, verbose_name='Preview', blank=True),
            preserve_default=True,
        ),
    ]
