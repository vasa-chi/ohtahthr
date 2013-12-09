# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Company'
        db.delete_table(u'ohthathr_company')


    def backwards(self, orm):
        # Adding model 'Company'
        db.create_table(u'ohthathr_company', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True)),
        ))
        db.send_create_signal(u'ohthathr', ['Company'])


    models = {
        
    }

    complete_apps = ['ohthathr']