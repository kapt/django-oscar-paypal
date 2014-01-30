# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PayPalFeesRate'
        db.create_table(u'paypal_paypalfeesrate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('min_sales_amount', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
            ('percentage', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=4)),
            ('fixed_amount', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
        ))
        db.send_create_signal(u'paypal', ['PayPalFeesRate'])


    def backwards(self, orm):
        # Deleting model 'PayPalFeesRate'
        db.delete_table(u'paypal_paypalfeesrate')


    models = {
        'paypal.expresstransaction': {
            'Meta': {'ordering': "('-date_created',)", 'object_name': 'ExpressTransaction'},
            'ack': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'amount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'correlation_id': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'error_code': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'error_message': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'raw_request': ('django.db.models.fields.TextField', [], {'max_length': '512'}),
            'raw_response': ('django.db.models.fields.TextField', [], {'max_length': '512'}),
            'response_time': ('django.db.models.fields.FloatField', [], {}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        },
        'paypal.payflowtransaction': {
            'Meta': {'ordering': "('-date_created',)", 'object_name': 'PayflowTransaction'},
            'amount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'authcode': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'avsaddr': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'avszip': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'comment1': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_index': 'True'}),
            'cvv2match': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pnref': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True'}),
            'ppref': ('django.db.models.fields.CharField', [], {'max_length': '32', 'unique': 'True', 'null': 'True'}),
            'raw_request': ('django.db.models.fields.TextField', [], {'max_length': '512'}),
            'raw_response': ('django.db.models.fields.TextField', [], {'max_length': '512'}),
            'respmsg': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'response_time': ('django.db.models.fields.FloatField', [], {}),
            'result': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'tender': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True'}),
            'trxtype': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        },
        u'paypal.paypalfeesrate': {
            'Meta': {'object_name': 'PayPalFeesRate'},
            'fixed_amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'min_sales_amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            'percentage': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '4'})
        }
    }

    complete_apps = ['paypal']