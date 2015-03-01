# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'pages_category')

        # Deleting model 'MerchantProducts'
        db.delete_table(u'pages_merchantproducts')

        # Deleting model 'Merchants'
        db.delete_table(u'pages_merchants')

        # Deleting model 'Features'
        db.delete_table(u'pages_features')

        # Deleting model 'ProductFeatures'
        db.delete_table(u'pages_productfeatures')

        # Deleting model 'ProductPrice'
        db.delete_table(u'pages_productprice')

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


    def backwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'pages_category', (
            ('subcategory', self.gf('django.db.models.fields.CharField')(max_length=400)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'pages', ['Category'])

        # Adding model 'MerchantProducts'
        db.create_table(u'pages_merchantproducts', (
            ('merchant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pages.Merchants'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('affiliate_url', self.gf('django.db.models.fields.URLField')(max_length=500)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('real_url', self.gf('django.db.models.fields.URLField')(max_length=500)),
            ('stock_status', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('logo_url', self.gf('django.db.models.fields.URLField')(default='http://urlnotgiven.com', max_length=500)),
        ))
        db.send_create_signal(u'pages', ['MerchantProducts'])

        # Adding model 'Merchants'
        db.create_table(u'pages_merchants', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('provider', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pages.Providers'])),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=500)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('logo_url', self.gf('django.db.models.fields.URLField')(max_length=500)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_joined', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'pages', ['Merchants'])

        # Adding model 'Features'
        db.create_table(u'pages_features', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'pages', ['Features'])

        # Adding model 'ProductFeatures'
        db.create_table(u'pages_productfeatures', (
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pages.MerchantProducts'])),
            ('feature', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pages.Features'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'pages', ['ProductFeatures'])

        # Adding model 'ProductPrice'
        db.create_table(u'pages_productprice', (
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pages.MerchantProducts'])),
            ('price', self.gf('django.db.models.fields.CharField')(default='0', max_length=10)),
            ('currency_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'pages', ['ProductPrice'])

        # Adding model 'Feeds'
        db.create_table(u'pages_feeds', (
            ('merchant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pages.Merchants'])),
            ('username', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('successful_download', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('file_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('password', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.TextField')()),
            ('provider', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pages.Providers'])),
            ('scheduled_at', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'pages', ['Feeds'])

        # Adding model 'Providers'
        db.create_table(u'pages_providers', (
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=500)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('logo_url', self.gf('django.db.models.fields.URLField')(max_length=500)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_joined', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'pages', ['Providers'])

        # Adding model 'Multipics'
        db.create_table(u'pages_multipics', (
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pages.MerchantProducts'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('image_url', self.gf('django.db.models.fields.URLField')(max_length=500)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('logo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'pages', ['Multipics'])

        # Adding model 'ProductCategory'
        db.create_table(u'pages_productcategory', (
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pages.Category'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pages.MerchantProducts'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'pages', ['ProductCategory'])

        # Adding model 'Brand'
        db.create_table(u'pages_brand', (
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=400)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal(u'pages', ['Brand'])


    models = {
        
    }

    complete_apps = ['pages']