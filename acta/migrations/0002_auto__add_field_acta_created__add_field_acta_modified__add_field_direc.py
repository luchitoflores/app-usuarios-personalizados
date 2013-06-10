# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Acta.created'
        db.add_column(u'acta_acta', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 6, 10, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Acta.modified'
        db.add_column(u'acta_acta', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 6, 10, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Direccion.created'
        db.add_column(u'acta_direccion', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 6, 10, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Direccion.modified'
        db.add_column(u'acta_direccion', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 6, 10, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Parroquia.created'
        db.add_column(u'acta_parroquia', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 6, 10, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Parroquia.modified'
        db.add_column(u'acta_parroquia', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 6, 10, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'NotaMarginal.created'
        db.add_column(u'acta_notamarginal', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 6, 10, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'NotaMarginal.modified'
        db.add_column(u'acta_notamarginal', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 6, 10, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Feligres.created'
        db.add_column(u'acta_feligres', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 6, 10, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Feligres.modified'
        db.add_column(u'acta_feligres', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 6, 10, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Acta.created'
        db.delete_column(u'acta_acta', 'created')

        # Deleting field 'Acta.modified'
        db.delete_column(u'acta_acta', 'modified')

        # Deleting field 'Direccion.created'
        db.delete_column(u'acta_direccion', 'created')

        # Deleting field 'Direccion.modified'
        db.delete_column(u'acta_direccion', 'modified')

        # Deleting field 'Parroquia.created'
        db.delete_column(u'acta_parroquia', 'created')

        # Deleting field 'Parroquia.modified'
        db.delete_column(u'acta_parroquia', 'modified')

        # Deleting field 'NotaMarginal.created'
        db.delete_column(u'acta_notamarginal', 'created')

        # Deleting field 'NotaMarginal.modified'
        db.delete_column(u'acta_notamarginal', 'modified')

        # Deleting field 'Feligres.created'
        db.delete_column(u'acta_feligres', 'created')

        # Deleting field 'Feligres.modified'
        db.delete_column(u'acta_feligres', 'modified')


    models = {
        u'acta.acta': {
            'Meta': {'object_name': 'Acta'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fecha_sacramento': ('django.db.models.fields.DateField', [], {}),
            'feligres': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Feligres'", 'to': u"orm['acta.Feligres']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lugar_celebracion': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'madrina': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Madrina'", 'to': u"orm['acta.Feligres']"}),
            'ministro': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'padrino': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Padrino'", 'to': u"orm['acta.Feligres']"}),
            'parroquia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['acta.Parroquia']"})
        },
        u'acta.direccion': {
            'Meta': {'object_name': 'Direccion'},
            'canton': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'ciudad': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'provincia': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'acta.feligres': {
            'Meta': {'object_name': 'Feligres'},
            'apellidos': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'cedula': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'estado_civil': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'fechaNacimiento': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lugarNacimiento': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'madre': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'Madre'", 'unique': 'True', 'null': 'True', 'to': u"orm['acta.Feligres']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'padre': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'Padre'", 'unique': 'True', 'null': 'True', 'to': u"orm['acta.Feligres']"}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'acta.notamarginal': {
            'Meta': {'object_name': 'NotaMarginal'},
            'acta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['acta.Acta']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'max_length': '400'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'acta.parroquia': {
            'Meta': {'object_name': 'Parroquia'},
            'ciudad': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['acta']