# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import plugins.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Plugin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('plugin_id', models.CharField(help_text='Plugin Id should be a 32 bit string with only A-Z or 0-9.', unique=True, max_length=50, verbose_name='Id')),
                ('name', models.CharField(unique=True, max_length=200, verbose_name='Name')),
                ('action_keyword', models.CharField(max_length=50, verbose_name='Default Action Keyword')),
                ('description', models.CharField(max_length=100, verbose_name='Description')),
                ('long_description', models.CharField(max_length=2000, verbose_name='Long Description', blank=True)),
                ('version', models.CharField(help_text='A version should be a MAJOR.MINOR.PATCH format. E.g. 1.0.0', max_length=20, verbose_name='Version')),
                ('language', models.CharField(max_length=20, verbose_name='Plugin language', choices=[('CSharp', 'CSharp'), ('Python', 'Python'), ('Other', 'Other')])),
                ('website', models.URLField(null=True, verbose_name='Plugin Website', blank=True)),
                ('enabled', models.BooleanField(default=True, verbose_name='Enabled')),
                ('private', models.BooleanField(default=False, help_text='User can only access pluign via plugin id', verbose_name='Private')),
                ('icon', models.ImageField(help_text='Only support .jpg and .png image', upload_to=plugins.models.get_file_path, verbose_name='Plugin Icon')),
                ('preview', models.ImageField(upload_to=plugins.models.get_file_path, null=True, verbose_name='Preview', blank=True)),
                ('github', models.URLField(null=True, verbose_name='github link', blank=True)),
                ('plugin_file', models.FileField(upload_to=plugins.models.get_file_path, max_length=500, verbose_name='Plugin file')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Create datetime')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Last modified datetime')),
                ('liked_count', models.IntegerField(default=0, verbose_name='Liked count')),
                ('created_by', models.ForeignKey(related_name='created_plugins', verbose_name='user', to=settings.AUTH_USER_MODEL)),
                ('liked_users', models.ManyToManyField(related_name='liked_plugins', verbose_name='Liked Users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
