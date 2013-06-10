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
            ('lugarNacimiento', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('fechaNacimiento', self.gf('django.db.models.fields.DateField')()),
            ('sexo', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('padre', self.gf('django.db.models.fields.related.OneToOneField')(blank=True, related_name='Padre', unique=True, null=True, to=orm['acta.Feligres'])),
            ('madre', self.gf('django.db.models.fields.related.OneToOneField')(blank=True, related_name='Madre', unique=True, null=True, to=orm['acta.Feligres'])),
            ('estado_civil', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'acta', ['Feligres'])

        # Adding model 'Parroquia'
        db.create_table(u'acta_parroquia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('ciudad', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'acta', ['Parroquia'])

        # Adding model 'Acta'
        db.create_table(u'acta_acta', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('ministro', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('feligres', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Feligres', to=orm['acta.Feligres'])),
            ('padrino', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Padrino', to=orm['acta.Feligres'])),
            ('madrina', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Madrina', to=orm['acta.Feligres'])),
            ('fecha_sacramento', self.gf('django.db.models.fields.DateField')()),
            ('lugar_celebracion', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('parroquia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['acta.Parroquia'])),
        ))
        db.send_create_signal(u'acta', ['Acta'])

        # Adding model 'NotaMarginal'
        db.create_table(u'acta_notamarginal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('acta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['acta.Acta'])),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(max_length=400)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'acta', ['NotaMarginal'])

        # Adding model 'Direccion'
        db.create_table(u'acta_direccion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('provincia', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('canton', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('ciudad', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('celular', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'acta', ['Direccion'])


    def backwards(self, orm):
        # Deleting model 'Feligres'
        db.delete_table(u'acta_feligres')

        # Deleting model 'Parroquia'
        db.delete_table(u'acta_parroquia')

        # Deleting model 'Acta'
        db.delete_table(u'acta_acta')

        # Deleting model 'NotaMarginal'
        db.delete_table(u'acta_notamarginal')

        # Deleting model 'Direccion'
        db.delete_table(u'acta_direccion')


    models = {
        u'acta.acta': {
            'Meta': {'object_name': 'Acta'},
            'fecha_sacramento': ('django.db.models.fields.DateField', [], {}),
            'feligres': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Feligres'", 'to': u"orm['acta.Feligres']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lugar_celebracion': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'madrina': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Madrina'", 'to': u"orm['acta.Feligres']"}),
            'ministro': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'padrino': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Padrino'", 'to': u"orm['acta.Feligres']"}),
            'parroquia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['acta.Parroquia']"})
        },
        u'acta.direccion': {
            'Meta': {'object_name': 'Direccion'},
            'canton': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'ciudad': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'provincia': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'acta.feligres': {
            'Meta': {'object_name': 'Feligres'},
            'apellidos': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'cedula': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'estado_civil': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'fechaNacimiento': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lugarNacimiento': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'madre': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'Madre'", 'unique': 'True', 'null': 'True', 'to': u"orm['acta.Feligres']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'padre': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'Padre'", 'unique': 'True', 'null': 'True', 'to': u"orm['acta.Feligres']"}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'acta.notamarginal': {
            'Meta': {'object_name': 'NotaMarginal'},
            'acta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['acta.Acta']"}),
            'descripcion': ('django.db.models.fields.TextField', [], {'max_length': '400'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'acta.parroquia': {
            'Meta': {'object_name': 'Parroquia'},
            'ciudad': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['acta']