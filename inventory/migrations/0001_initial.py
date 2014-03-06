# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'InventoryLocation'
        db.create_table(u'inventory_inventorylocation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('location_code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32)),
        ))
        db.send_create_signal(u'inventory', ['InventoryLocation'])

        # Adding model 'InventoryItem'
        db.create_table(u'inventory_inventoryitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('part_number', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('part_type', self.gf('django.db.models.fields.CharField')(default='M', max_length=1)),
            ('stocking_uom', self.gf('django.db.models.fields.CharField')(default='EA', max_length=4)),
            ('purchasing_uom', self.gf('django.db.models.fields.CharField')(default='EA', max_length=4)),
            ('part_weight', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=10)),
        ))
        db.send_create_signal(u'inventory', ['InventoryItem'])

        # Adding model 'ItemCrossReference'
        db.create_table(u'inventory_itemcrossreference', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.InventoryItem'])),
            ('cross_reference', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal(u'inventory', ['ItemCrossReference'])

        # Adding model 'InventoryTag'
        db.create_table(u'inventory_inventorytag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag_number', self.gf('django.db.models.fields.IntegerField')()),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.InventoryItem'])),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.InventoryLocation'])),
            ('lot_number', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quality.Report'])),
            ('vendor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['purchasing.Vendor'])),
            ('unit_cost', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=10)),
            ('receiving_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('quantity', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=10)),
        ))
        db.send_create_signal(u'inventory', ['InventoryTag'])

        # Adding model 'RoutingStep'
        db.create_table(u'inventory_routingstep', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('part', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.InventoryItem'])),
            ('step_number', self.gf('django.db.models.fields.IntegerField')()),
            ('setup_time', self.gf('django.db.models.fields.IntegerField')()),
            ('setup_interval', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('cycle_time', self.gf('django.db.models.fields.IntegerField')()),
            ('cycle_interval', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'inventory', ['RoutingStep'])


    def backwards(self, orm):
        # Deleting model 'InventoryLocation'
        db.delete_table(u'inventory_inventorylocation')

        # Deleting model 'InventoryItem'
        db.delete_table(u'inventory_inventoryitem')

        # Deleting model 'ItemCrossReference'
        db.delete_table(u'inventory_itemcrossreference')

        # Deleting model 'InventoryTag'
        db.delete_table(u'inventory_inventorytag')

        # Deleting model 'RoutingStep'
        db.delete_table(u'inventory_routingstep')


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
        u'inventory.itemcrossreference': {
            'Meta': {'object_name': 'ItemCrossReference'},
            'cross_reference': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.InventoryItem']"})
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