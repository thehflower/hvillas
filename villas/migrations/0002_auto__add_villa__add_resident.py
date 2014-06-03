# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Villa'
        db.create_table('villas_villa', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('feet', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal('villas', ['Villa'])

        # Adding model 'Resident'
        db.create_table('villas_resident', (
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=50)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('villa', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, primary_key=True, to=orm['villas.Villa'])),
        ))
        db.send_create_signal('villas', ['Resident'])


    def backwards(self, orm):
        # Deleting model 'Villa'
        db.delete_table('villas_villa')

        # Deleting model 'Resident'
        db.delete_table('villas_resident')


    models = {
        'villas.resident': {
            'Meta': {'object_name': 'Resident'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'villa': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'primary_key': 'True', 'to': "orm['villas.Villa']"})
        },
        'villas.villa': {
            'Meta': {'object_name': 'Villa'},
            'feet': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['villas']