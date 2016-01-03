# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'TeaserItem.url_title'
        db.add_column(u'contentitem_fluentcms_teaser_teaseritem', 'url_title',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'TeaserItem.url_title'
        db.delete_column(u'contentitem_fluentcms_teaser_teaseritem', 'url_title')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'fluent_contents.contentitem': {
            'Meta': {'ordering': "(u'placeholder', u'sort_order')", 'object_name': 'ContentItem'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '15', 'db_index': 'True'}),
            'parent_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'parent_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'contentitems'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['fluent_contents.Placeholder']"}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'polymorphic_fluent_contents.contentitem_set+'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'default': '1', 'db_index': 'True'})
        },
        u'fluent_contents.placeholder': {
            'Meta': {'unique_together': "((u'parent_type', u'parent_id', u'slot'),)", 'object_name': 'Placeholder'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'parent_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            'role': ('django.db.models.fields.CharField', [], {'default': "u'm'", 'max_length': '1'}),
            'slot': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'fluentcms_teaser.teaseritem': {
            'Meta': {'ordering': "(u'placeholder', u'sort_order')", 'object_name': 'TeaserItem', 'db_table': "u'contentitem_fluentcms_teaser_teaseritem'", '_ormbases': [u'fluent_contents.ContentItem']},
            u'contentitem_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['fluent_contents.ContentItem']", 'unique': 'True', 'primary_key': 'True'}),
            'description': ('fluent_contents.extensions.PluginHtmlField', [], {'null': 'True', 'blank': 'True'}),
            'image': ('fluent_contents.extensions.PluginImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'target': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'url': ('fluent_contents.extensions.PluginUrlField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'url_title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['fluentcms_teaser']