# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Feligres.fecha_nacimiento'
        db.delete_column(u'acta_feligres', 'fecha_nacimiento')

        # Adding field 'Feligres.lugarNacimiento'
        db.add_column(u'acta_feligres', 'lugarNacimiento',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Feligres.fechaNacimiento'
        db.add_column(u'acta_feligres', 'fechaNacimiento',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Feligres.fecha_nacimiento'
        db.add_column(u'acta_feligres', 'fecha_nacimiento',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 5, 20, 0, 0)),
                      keep_default=False)

        # Deleting field 'Feligres.lugarNacimiento'
        db.delete_column(u'acta_feligres', 'lugarNacimiento')

        # Deleting field 'Feligres.fechaNacimiento'
        db.delete_column(u'acta_feligres', 'fechaNacimiento')


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
            'fechaNacimiento': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lugarNacimiento': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
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