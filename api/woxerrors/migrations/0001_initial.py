# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Error',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('detail', models.CharField(max_length=3000, verbose_name='Error detail')),
                ('is_solved', models.BooleanField(default=False, verbose_name='Is s olved')),
                ('count', models.IntegerField(default=0, verbose_name='Count')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Create datetime')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Last modified datetime')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ErrorReproduceStep',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('step_detail', models.CharField(max_length=3000, verbose_name='step detail')),
                ('error', models.ForeignKey(verbose_name='error', to='woxerrors.Error')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
