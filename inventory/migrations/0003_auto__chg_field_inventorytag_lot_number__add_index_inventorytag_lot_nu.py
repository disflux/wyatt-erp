# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Renaming column for 'InventoryTag.lot_number' to match new field type.
        db.rename_column(u'inventory_inventorytag', 'lot_number', 'lot_number_id')
        # Changing field 'InventoryTag.lot_number'
        db.alter_column(u'inventory_inventorytag', 'lot_number_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quality.Report']))
        # Adding index on 'InventoryTag', fields ['lot_number']
        db.create_index(u'inventory_inventorytag', ['lot_number_id'])


    def backwards(self, orm):
        # Removing index on 'InventoryTag', fields ['lot_number']
        db.delete_index(u'inventory_inventorytag', ['lot_number_id'])


        # Renaming column for 'InventoryTag.lot_number' to match new field type.
        db.rename_column(u'inventory_inventorytag', 'lot_number_id', 'lot_number')
        # Changing field 'InventoryTag.lot_number'
        db.alter_column(u'inventory_inventorytag', 'lot_number', self.gf('django.db.models.fields.CharField')(max_length=16))

    models = {
        u'inventory.inventoryitem': {
            'Meta': {'object_name': 'InventoryItem'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'part_number': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'part_type': ('django.db.models.fields.CharField', [], {'default': "'M'", 'max_length': '1'}),
            'part_weight': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '10'}),
            'purchasing_uom': ('django.db.models.fields.CharField', [], {'default': "'EA'", 'max_length': '4'}),
            'stocking_uom': ('django.db.models.fields.CharField', [], {'default': "'EA'", 'max_length': '4'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'inventory.inventorylocation': {
            'Meta': {'object_name': 'InventoryLocation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'})
        },
        u'inventory.inventorytag': {
            'Meta': {'object_name': 'InventoryTag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.InventoryItem']"}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.InventoryLocation']"}),
            'lot_number': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quality.Report']"}),
            'quantity': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '10'}),
            'receiving_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'tag_number': ('django.db.models.fields.IntegerField', [], {}),
            'unit_cost': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '10'}),
            'vendor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['purchasing.Vendor']"})
        },
        u'inventory.routingstep': {
            'Meta': {'ordering': "['step_number']", 'object_name': 'RoutingStep'},
            'cycle_interval': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'cycle_time': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'part': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.InventoryItem']"}),
            'setup_interval': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'setup_time': ('django.db.models.fields.IntegerField', [], {}),
            'step_number': ('django.db.models.fields.IntegerField', [], {})
        },
        u'purchasing.vendor': {
            'Meta': {'object_name': 'Vendor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'quality.report': {
            'Meta': {'object_name': 'Report'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lot_number': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        }
    }

    complete_apps = ['inventory']