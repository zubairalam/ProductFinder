# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'pages_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('subcategory', self.gf('django.db.models.fields.CharField')(max_length=400)),
        ))
        db.send_create_signal(u'pages', ['Category'])

        # Adding model 'ProductPrice'
        db.create_table(u'pages_productprice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pages.MerchantProducts'])),
            ('price', self.gf('django.db.models.fields.CharField')(default='0', max_length=10)),
            ('currency_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'pages', ['ProductPrice'])

        # Adding model 'Merchants'
        db.create_table(u'pages_merchants', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('provider', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pages.Providers'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('date_joined', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=500)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('logo_url', self.gf('django.db.models.fields.URLField')(max_length=500)),
        ))
        db.send_create_signal(u'pages', ['Merchants'])

        # Adding model 'Features'
        db.create_table(u'pages_features', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal(u'pages', ['Features'])

        # Adding model 'ProductFeatures'
        db.create_table(u'pages_productfeatures', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pages.MerchantProducts'])),
            ('feature', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pages.Features'])),
        ))
        db.send_create_signal(u'pages', ['ProductFeatures'])

        # Adding model 'MerchantProducts'
        db.create_table(u'pages_merchantproducts', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('merchant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pages.Merchants'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('stock_status', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('logo_url', self.gf('django.db.models.fields.URLField')(default='http://urlnotgiven.com', max_length=500)),
            ('affiliate_url', self.gf('django.db.models.fields.URLField')(max_length=500)),
            ('real_url', self.gf('django.db.models.fields.URLField')(max_length=500)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'pages', ['MerchantProducts'])

        # Adding model 'Feeds'
        db.create_table(u'pages_feeds', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('provider', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pages.Providers'])),
            ('merchant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pages.Merchants'])),
            ('file_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('url', self.gf('django.db.models.fields.TextField')()),
            ('username', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('password', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('scheduled_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('successful_download', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'pages', ['Feeds'])

        # Adding model 'Providers'
        db.create_table(u'pages_providers', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('date_joined', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=500)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('logo_url', self.gf('django.db.models.fields.URLField')(max_length=500)),
        ))
        db.send_create_signal(u'pages', ['Providers'])

        # Adding model 'Multipics'
        db.create_table(u'pages_multipics', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pages.MerchantProducts'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('image_url', self.gf('django.db.models.fields.URLField')(max_length=500)),
            ('logo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'pages', ['Multipics'])

        # Adding model 'ProductCategory'
        db.create_table(u'pages_productcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pages.MerchantProducts'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pages.Category'])),
        ))
        db.send_create_signal(u'pages', ['ProductCategory'])

        # Adding model 'Brand'
        db.create_table(u'pages_brand', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=400)),
        ))
        db.send_create_signal(u'pages', ['Brand'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'pages_category')

        # Deleting model 'ProductPrice'
        db.delete_table(u'pages_productprice')

        # Deleting model 'Merchants'
        db.delete_table(u'pages_merchants')

        # Deleting model 'Features'
        db.delete_table(u'pages_features')

        # Deleting model 'ProductFeatures'
        db.delete_table(u'pages_productfeatures')

        # Deleting model 'MerchantProducts'
        db.delete_table(u'pages_merchantproducts')

        # Deleting model 'Feeds'
        db.delete_table(u'pages_feeds')

        # Deleting model 'Providers'
        db.delete_table(u'pages_providers')

        # Deleting model 'Multipics'
        db.delete_table(u'pages_multipics')

        # Deleting model 'ProductCategory'
        db.delete_table(u'pages_productcategory')

        # Deleting model 'Brand'
        db.delete_table(u'pages_brand')


    models = {
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
            'provider': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pages.Providers']"}),
            'scheduled_at': ('django.db.models.fields.DateTimeField', [], {}),
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
            'logo_url': ('django.db.models.fields.URLField', [], {'max_length': '500'}),
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
            'logo_url': ('django.db.models.fields.URLField', [], {'max_length': '500'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['pages']