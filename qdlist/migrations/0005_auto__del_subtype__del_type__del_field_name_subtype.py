# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'subtype'
        db.delete_table(u'qdlist_subtype')

        # Deleting model 'type'
        db.delete_table(u'qdlist_type')

        # Deleting field 'name.subtype'
        db.delete_column(u'qdlist_name', 'subtype_id')


    def backwards(self, orm):
        # Adding model 'subtype'
        db.create_table(u'qdlist_subtype', (
            ('subtypename', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['qdlist.type'], null=True)),
            ('subtype_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subtypedescription', self.gf('django.db.models.fields.CharField')(max_length=25)),
        ))
        db.send_create_signal(u'qdlist', ['subtype'])

        # Adding model 'type'
        db.create_table(u'qdlist_type', (
            ('typename', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('type_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'qdlist', ['type'])

        # Adding field 'name.subtype'
        db.add_column(u'qdlist_name', 'subtype',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['qdlist.subtype'], null=True),
                      keep_default=False)


    models = {
        u'qdlist.links': {
            'DomainLinkName': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'Link_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'Meta': {'object_name': 'links'}
        },
        u'qdlist.name': {
            'Meta': {'object_name': 'name'},
            'NameDocument': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'NameDocumentFull': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'Name_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'qdlist.quantizeddoc': {
            'Link': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['qdlist.links']", 'null': 'True'}),
            'Meta': {'object_name': 'quantizeddoc'},
            'Name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['qdlist.name']", 'null': 'True'}),
            'QDDate': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'QDNumExtra': ('django.db.models.fields.CharField', [], {'max_length': '11', 'null': 'True'}),
            'QDNumFromPublication': ('django.db.models.fields.CharField', [], {'max_length': '11', 'null': 'True'}),
            'QDNumSerial': ('django.db.models.fields.CharField', [], {'max_length': '11', 'null': 'True'}),
            'QuantizedDoc_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'Year': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['qdlist.years']"})
        },
        u'qdlist.years': {
            'Meta': {'object_name': 'years'},
            'YearName': ('django.db.models.fields.IntegerField', [], {}),
            'Year_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['qdlist']