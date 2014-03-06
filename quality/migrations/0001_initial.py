# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Report'
        db.create_table(u'quality_report', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lot_number', self.gf('django.db.models.fields.CharField')(max_length=16)),
        ))
        db.send_create_signal(u'quality', ['Report'])


    def backwards(self, orm):
        # Deleting model 'Report'
        db.delete_table(u'quality_report')


    models = {
        u'quality.report': {
            'Meta': {'object_name': 'Report'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lot_number': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        }
    }

    complete_apps = ['quality']