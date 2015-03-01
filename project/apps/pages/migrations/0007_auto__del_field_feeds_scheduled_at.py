# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Feeds.scheduled_at'
        db.delete_column(u'pages_feeds', 'scheduled_at')


    def backwards(self, orm):
        # Adding field 'Feeds.scheduled_at'
        db.add_column(u'pages_feeds', 'scheduled_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=''),
                      keep_default=False)


    models = {
        u'djcelery.crontabschedule': {
            'Meta': {'ordering': "[u'month_of_year', u'day_of_month', u'day_of_week', u'hour', u'minute']", 'object_name': 'CrontabSchedule'},
            'day_of_month': ('django.db.models.fields.CharField', [], {'default': "u'*'", 'max_length': '64'}),
            'day_of_week': ('django.db.models.fields.CharField', [], {'default': "u'*'", 'max_length': '64'}),
            'hour': ('django.db.models.fields.CharField', [], {'default': "u'*'", 'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minute': ('django.db.models.fields.CharField', [], {'default': "u'*'", 'max_length': '64'}),
            'month_of_year': ('django.db.models.fields.CharField', [], {'default': "u'*'", 'max_length': '64'})
        },
        u'djcelery.intervalschedule': {
            'Meta': {'ordering': "[u'period', u'every']", 'object_name': 'IntervalSchedule'},
            'every': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'period': ('django.db.models.fields.CharField', [], {'max_length': '24'})
        },
        u'djcelery.periodictask': {
            'Meta': {'object_name': 'PeriodicTask'},
            'args': ('django.db.models.fields.TextField', [], {'default': "u'[]'", 'blank': 'True'}),
            'crontab': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['djcelery.CrontabSchedule']", 'null': 'True', 'blank': 'True'}),
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'exchange': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'expires': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interval': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['djcelery.IntervalSchedule']", 'null': 'True', 'blank': 'True'}),
            'kwargs': ('django.db.models.fields.TextField', [], {'default': "u'{}'", 'blank': 'True'}),
            'last_run_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'queue': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'routing_key': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'task': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'total_run_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'pages.brand': {
            'Meta': {'object_name': 'Brand'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '400'})
        },
        u'pages.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'subcategory': ('django.db.models.fields.CharField', [], {'max_length': '400'})
        },
        u'pages.features': {
            'Meta': {'object_name': 'Features'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'pages.feeds': {
            'Meta': {'object_name': 'Feeds'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'file_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'merchant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pages.Merchants']"}),
            'password': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'periodic_task': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['djcelery.PeriodicTask']", 'null': 'True'}),
            'provider': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pages.Providers']"}),
            'successful_download': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'url': ('django.db.models.fields.TextField', [], {}),
            'username': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'})
        },
        u'pages.merchantproducts': {
            'Meta': {'object_name': 'MerchantProducts'},
            'affiliate_url': ('django.db.models.fields.URLField', [], {'max_length': '500'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'logo_url': ('django.db.models.fields.URLField', [], {'default': "'http://urlnotgiven.com'", 'max_length': '500'}),
            'merchant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pages.Merchants']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'real_url': ('django.db.models.fields.URLField', [], {'max_length': '500'}),
            'stock_status': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'pages.merchants': {
            'Meta': {'object_name': 'Merchants'},
            'date_joined': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'provider': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pages.Providers']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '500'})
        },
        u'pages.multipics': {
            'Meta': {'object_name': 'Multipics'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'image_url': ('django.db.models.fields.URLField', [], {'max_length': '500'}),
            'logo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pages.MerchantProducts']"}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'pages.productcategory': {
            'Meta': {'object_name': 'ProductCategory'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pages.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pages.MerchantProducts']"})
        },
        u'pages.productfeatures': {
            'Meta': {'object_name': 'ProductFeatures'},
            'feature': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pages.Features']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pages.MerchantProducts']"})
        },
        u'pages.productprice': {
            'Meta': {'object_name': 'ProductPrice'},
            'currency_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '10'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pages.MerchantProducts']"}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'pages.providers': {
            'Meta': {'object_name': 'Providers'},
            'date_joined': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['pages']