# -*- coding: utf-8 -*-
from django.db import models
from django.core.cache import cache
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class Commit(models.Model):
    revision = models.CharField(_('revision'), max_length=40)
    comments = models.TextField(_('comments'))

    crdate = models.DateTimeField(_('date created'), auto_now_add=True)
    tstamp = models.DateTimeField(_('date edited'), auto_now=True)

    def __unicode__(self):
        return self.description

class Build(models.Model):
    commit = models.ForeignKey(Commit)
    number = models.IntegerField(_('number'))
    builder = models.CharField(_('builder'), max_length=50)

    crdate = models.DateTimeField(_('date created'), auto_now_add=True)
    tstamp = models.DateTimeField(_('date edited'), auto_now=True)

    def __unicode__(self):
        return u'%s:%d' % (self.builder, self.number)

class Tag(models.Model):
    commit = models.ForeignKey(Commit)
    name = models.CharField(_('name'), max_length=50)

    crdate = models.DateTimeField(_('date created'), auto_now_add=True)
    tstamp = models.DateTimeField(_('date edited'), auto_now=True)

    def __unicode__(self):
        return self.name
