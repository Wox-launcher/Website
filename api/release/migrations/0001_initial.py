# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.CharField(help_text='A version should be a MAJOR.MINOR.PATCH format. E.g. 1.0.0', unique=True, max_length=20, verbose_name='Version')),
                ('download_link', models.URLField()),
                ('download_link1', models.URLField(verbose_name='Backup download link 1', blank=True)),
                ('download_link2', models.URLField(verbose_name='Backup download link 2', blank=True)),
                ('description', models.CharField(max_length=1000, blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_date'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UpgradeRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.CharField(max_length=30)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_date'],
            },
            bases=(models.Model,),
        ),
    ]
