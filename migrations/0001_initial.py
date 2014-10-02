# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('builds', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50, verbose_name='Name')),
            ],
            options={
                'ordering': ('name',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Flavor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50, verbose_name='Name')),
                ('download_root', models.FilePathField(recursive=True, allow_files=False, max_length=250, allow_folders=True, path=b'D:\\Web\\django-marcsupdater\\marcsupdater\\_static', verbose_name='Download root')),
                ('download_path', models.URLField(max_length=250, verbose_name='Download path')),
                ('application', models.ForeignKey(related_name=b'flavors', to='downloads.Application')),
                ('builder', models.ForeignKey(related_name=b'flavors', to='builds.Builder')),
            ],
            options={
                'ordering': ('name',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50, verbose_name='Name')),
                ('date', models.DateTimeField(verbose_name='Date')),
                ('stable', models.BooleanField(default=False, verbose_name='Stable')),
                ('changes', models.TextField(null=True, verbose_name='Changes', blank=True)),
                ('build', models.ForeignKey(related_name=b'versions', to='builds.Build')),
                ('flavor', models.ForeignKey(related_name=b'versions', to='downloads.Flavor')),
            ],
            options={
                'ordering': ('-date',),
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='version',
            unique_together=set([('flavor', 'build')]),
        ),
        migrations.AlterUniqueTogether(
            name='flavor',
            unique_together=set([('application', 'builder')]),
        ),
    ]
