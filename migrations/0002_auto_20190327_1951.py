# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-27 19:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('downloads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flavor',
            name='download_root',
            field=models.FilePathField(allow_files=False, allow_folders=True, max_length=250, path='/Users/marc/Workspaces/Web/django-marcsupdater/marcsupdater/_static', recursive=True, verbose_name='Download root'),
        ),
    ]