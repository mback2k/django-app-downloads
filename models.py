# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from ..builds.models import Builder, Build
import os.path, urllib

class Application(models.Model):
    name = models.CharField(_('Name'), max_length=50, unique=True)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name

class Flavor(models.Model):
    DOWNLOAD_ROOT = getattr(settings, 'DOWNLOAD_ROOT', settings.STATIC_ROOT)

    application = models.ForeignKey(Application, related_name='flavors')
    builder = models.ForeignKey(Builder, related_name='flavors')
    name = models.CharField(_('Name'), max_length=50, unique=True)
    download_root = models.FilePathField(_('Download root'), path=DOWNLOAD_ROOT, recursive=True, allow_files=False, allow_folders=True, max_length=250)
    download_path = models.URLField(_('Download path'), max_length=250)

    class Meta:
        ordering = ('name',)
        unique_together = ('application', 'builder')

    def __unicode__(self):
        return self.name

class Version(models.Model):
    flavor = models.ForeignKey(Flavor, related_name='versions')
    build = models.ForeignKey(Build, related_name='versions')
    name = models.CharField(_('Name'), max_length=50, unique=True)
    date = models.DateTimeField(_('Date'))
    stable = models.BooleanField(_('Stable'), default=False)
    changes = models.TextField(_('Changes'), blank=True, null=True)

    class Meta:
        ordering = ('-date',)
        unique_together = ('flavor', 'build')

    def __unicode__(self):
        return self.name

    @property
    def download_url(self):
        filename = '%s.exe' % self.flavor.application.name
        build_number = str(self.build.number)

        download_file = os.path.join(self.flavor.download_root, build_number, filename)
        if os.path.exists(download_file):
            download_url = os.path.join(self.flavor.download_path, build_number, urllib.quote(filename))
            return download_url

        for change in self.build.changes:
            download_file = os.path.join(self.flavor.download_root, change.revision, build_number, filename)
            if os.path.exists(download_file):
                download_url = os.path.join(self.flavor.download_path, change.revision, build_number, urllib.quote(filename))
                return download_url

        return None
