# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Application'
        db.create_table(u'downloads_application', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'downloads', ['Application'])

        # Adding model 'Flavor'
        db.create_table(u'downloads_flavor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('application', self.gf('django.db.models.fields.related.ForeignKey')(related_name='flavors', to=orm['downloads.Application'])),
            ('builder', self.gf('django.db.models.fields.related.ForeignKey')(related_name='flavors', to=orm['builds.Builder'])),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('download_root', self.gf('django.db.models.fields.FilePathField')(path='/srv/www/de/marc-hoersken/updater/download/', max_length=250, recursive=True)),
            ('download_path', self.gf('django.db.models.fields.URLField')(max_length=250)),
        ))
        db.send_create_signal(u'downloads', ['Flavor'])

        # Adding unique constraint on 'Flavor', fields ['application', 'builder']
        db.create_unique(u'downloads_flavor', ['application_id', 'builder_id'])

        # Adding model 'Version'
        db.create_table(u'downloads_version', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('flavor', self.gf('django.db.models.fields.related.ForeignKey')(related_name='versions', to=orm['downloads.Flavor'])),
            ('build', self.gf('django.db.models.fields.related.ForeignKey')(related_name='versions', to=orm['builds.Build'])),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('stable', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('changes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'downloads', ['Version'])

        # Adding unique constraint on 'Version', fields ['flavor', 'build']
        db.create_unique(u'downloads_version', ['flavor_id', 'build_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Version', fields ['flavor', 'build']
        db.delete_unique(u'downloads_version', ['flavor_id', 'build_id'])

        # Removing unique constraint on 'Flavor', fields ['application', 'builder']
        db.delete_unique(u'downloads_flavor', ['application_id', 'builder_id'])

        # Deleting model 'Application'
        db.delete_table(u'downloads_application')

        # Deleting model 'Flavor'
        db.delete_table(u'downloads_flavor')

        # Deleting model 'Version'
        db.delete_table(u'downloads_version')


    models = {
        u'builds.build': {
            'Meta': {'ordering': "('-start_time',)", 'unique_together': "(('builder', 'number'),)", 'object_name': 'Build'},
            'builder': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'builds'", 'to': u"orm['builds.Builder']"}),
            'changes': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'builds'", 'symmetrical': 'False', 'to': u"orm['builds.Change']"}),
            'completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'data': ('django.db.models.fields.TextField', [], {}),
            'duration': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'properties': ('django.db.models.fields.TextField', [], {}),
            'result': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'simplified_result': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'builds.builder': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Builder'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'builds.change': {
            'Meta': {'ordering': "('-when',)", 'unique_together': "(('project', 'repository', 'revision'),)", 'object_name': 'Change'},
            'comments': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'changes'", 'to': u"orm['builds.Project']"}),
            'repository': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'changes'", 'null': 'True', 'to': u"orm['builds.Repository']"}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'when': ('django.db.models.fields.DateTimeField', [], {}),
            'who': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'builds.project': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Project'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'builds.repository': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Repository'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'})
        },
        u'downloads.application': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Application'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'downloads.flavor': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('application', 'builder'),)", 'object_name': 'Flavor'},
            'application': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'flavors'", 'to': u"orm['downloads.Application']"}),
            'builder': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'flavors'", 'to': u"orm['builds.Builder']"}),
            'download_path': ('django.db.models.fields.URLField', [], {'max_length': '250'}),
            'download_root': ('django.db.models.fields.FilePathField', [], {'path': "'/srv/www/de/marc-hoersken/updater/download/'", 'max_length': '250', 'recursive': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'downloads.version': {
            'Meta': {'ordering': "('-date',)", 'unique_together': "(('flavor', 'build'),)", 'object_name': 'Version'},
            'build': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'versions'", 'to': u"orm['builds.Build']"}),
            'changes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'flavor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'versions'", 'to': u"orm['downloads.Flavor']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'stable': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['downloads']