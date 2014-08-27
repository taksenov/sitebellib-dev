# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'type'
        db.create_table(u'qdlist_type', (
            ('type_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('typename', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'qdlist', ['type'])

        # Adding model 'subtype'
        db.create_table(u'qdlist_subtype', (
            ('subtype_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subtypename', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('subtypedescription', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('type_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['qdlist.type'])),
        ))
        db.send_create_signal(u'qdlist', ['subtype'])

        # Adding model 'quantizeddoc'
        db.create_table(u'qdlist_quantizeddoc', (
            ('QuantizedDoc_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['qdlist.name'], null=True)),
            ('Year', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['qdlist.years'])),
            ('QDNumSerial', self.gf('django.db.models.fields.CharField')(max_length=11, null=True)),
            ('QDNumFromPublication', self.gf('django.db.models.fields.CharField')(max_length=11, null=True)),
            ('QDDate', self.gf('django.db.models.fields.DateField')(null=True)),
            ('QDNumExtra', self.gf('django.db.models.fields.CharField')(max_length=11, null=True)),
            ('Link', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['qdlist.links'], null=True)),
        ))
        db.send_create_signal(u'qdlist', ['quantizeddoc'])

        # Adding model 'name'
        db.create_table(u'qdlist_name', (
            ('Name_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('NameDocument', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('NameDocumentFull', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('subtype_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['qdlist.subtype'])),
        ))
        db.send_create_signal(u'qdlist', ['name'])

        # Adding model 'years'
        db.create_table(u'qdlist_years', (
            ('Year_id', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True)),
            ('YearName', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'qdlist', ['years'])

        # Adding model 'links'
        db.create_table(u'qdlist_links', (
            ('Link_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('DomainLinkName', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'qdlist', ['links'])


    def backwards(self, orm):
        # Deleting model 'type'
        db.delete_table(u'qdlist_type')

        # Deleting model 'subtype'
        db.delete_table(u'qdlist_subtype')

        # Deleting model 'quantizeddoc'
        db.delete_table(u'qdlist_quantizeddoc')

        # Deleting model 'name'
        db.delete_table(u'qdlist_name')

        # Deleting model 'years'
        db.delete_table(u'qdlist_years')

        # Deleting model 'links'
        db.delete_table(u'qdlist_links')


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
            'Name_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subtype_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['qdlist.subtype']"})
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
        u'qdlist.subtype': {
            'Meta': {'object_name': 'subtype'},
            'subtype_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subtypedescription': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'subtypename': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'type_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['qdlist.type']"})
        },
        u'qdlist.type': {
            'Meta': {'object_name': 'type'},
            'type_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'typename': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'qdlist.years': {
            'Meta': {'object_name': 'years'},
            'YearName': ('django.db.models.fields.IntegerField', [], {}),
            'Year_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['qdlist']