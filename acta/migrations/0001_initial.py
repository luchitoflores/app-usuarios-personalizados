# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Feligres'
        db.create_table(u'acta_feligres', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cedula', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('apellidos', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('fecha_nacimiento', self.gf('django.db.models.fields.DateField')()),
            ('sexo', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'acta', ['Feligres'])

        # Adding model 'Acta'
        db.create_table(u'acta_acta', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('feligres', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['acta.Feligres'])),
            ('padrino', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('madrina', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'acta', ['Acta'])

        # Adding model 'Parroquia'
        db.create_table(u'acta_parroquia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('ciudad', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'acta', ['Parroquia'])


    def backwards(self, orm):
        # Deleting model 'Feligres'
        db.delete_table(u'acta_feligres')

        # Deleting model 'Acta'
        db.delete_table(u'acta_acta')

        # Deleting model 'Parroquia'
        db.delete_table(u'acta_parroquia')


    models = {
        u'acta.acta': {
            'Meta': {'object_name': 'Acta'},
            'feligres': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['acta.Feligres']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'madrina': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'padrino': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'acta.feligres': {
            'Meta': {'object_name': 'Feligres'},
            'apellidos': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'cedula': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'acta.parroquia': {
            'Meta': {'object_name': 'Parroquia'},
            'ciudad': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['acta']