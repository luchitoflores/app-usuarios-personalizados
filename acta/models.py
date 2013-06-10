# -*- coding:utf-8 -*-
from django.db import models
from django.conf import settings

from .validators import validate_cedula

class TimeStampedModel(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True


class ActaManager(models.Manager):
	def actas_por_anio(self, anio):
		return self.model.objects.filter(fecha_sacramento__year=anio)



class Feligres(TimeStampedModel):
	SEXO_CHOICES    = (
		('m','Masculino'),('f','Femenino')
		)

	ESTADOCIVIL_CHOICES    = (
		('s','Soltero/a'),('c','Casado/a'),('d','Divorciado/a'),('v','Viudo/a')
		)


	cedula          = models.CharField(max_length=30, help_text='Ingrese un numero de cedula ej:1104688617', unique=True, 
					error_messages  ={'unique': 'Ya existe un feligrés con ese número de cédula'},
					validators=[validate_cedula])
	nombre          = models.CharField(max_length=30,help_text='Ingrese un nombre ej:Jose, Edison')
	apellidos       = models.CharField(max_length=30,help_text='Ingrese apellidos ej: Espinosa, Espinosa Luna')
	lugarNacimiento = models.CharField(max_length=100, verbose_name=u'Lugar de Nacimiento', help_text='Ingrese el lugar de nacimiento')
	fechaNacimiento = models.DateField(verbose_name=u'Fecha de Nacimiento', help_text='Ingrese la Fecha de nacimiento')
	sexo            = models.CharField(max_length=30,choices=SEXO_CHOICES)
	padre        = models.OneToOneField('Feligres', related_name='Padre', blank=True, null=True, limit_choices_to={'sexo__contains':'m'})
	madre        = models.OneToOneField('Feligres', related_name='Madre', blank=True, null=True, limit_choices_to={'sexo__contains':'f'})
	estado_civil = models.CharField('EStado Civil', max_length=100, choices=ESTADOCIVIL_CHOICES)


	#def __unicode__(self):
	#	return self.nombre

	def __str__(self):
		return self.nombre
	def get_absolute_url(self):
		return "/feligres/%i/" % self.id

	class Meta:
		verbose_name=u'Feligres'
		verbose_name_plural = 'Feligreses'

class Parroquia(TimeStampedModel):
	nombre =models.CharField(max_length=30, help_text='Ej. San Bartolomé de Amaluza')
	ciudad =models.CharField(max_length=30, help_text='Amaluza')
	#def __unicode__(self):
	#	return self.nombre
	
	def __str__(self):
		return self.nombre

	def get_absolute_url(self):
		return '/parroquia/%i' %(self.id)

	class Meta:
		permissions = (
							('acta.add_parroquia', 'Puede crear una parroquia'),
							('acta.change_parroquia', 'Puede actualizar la parroquia'),
					  )

		verbose_name=u'Parroquia'
		verbose_name_plural= 'Parroquias'


class Acta(TimeStampedModel):
	numero   = models.CharField(max_length=30)
	ministro = models.CharField(max_length=30)
	feligres = models.ForeignKey(Feligres, related_name='Feligres')
	padrino  = models.ForeignKey(Feligres, related_name='Padrino', limit_choices_to={'sexo__contains':'m'})
	madrina  = models.ForeignKey(Feligres, related_name='Madrina', limit_choices_to={'sexo__contains':'f'})
	fecha_sacramento = models.DateField()
	lugar_celebracion = models.CharField(max_length=30)
	parroquia = models.ForeignKey('Parroquia')
	#def __unicode__(self):
	#	return self.numero
	
	objects = ActaManager()	
	
	
	def __str__(self):
		return self.numero

class NotaMarginal(TimeStampedModel):
	acta = models.ForeignKey('Acta')
	titulo = models.CharField(max_length=30)
	descripcion = models.TextField(max_length=400)
	fecha = models.DateField()

class Direccion(TimeStampedModel):
	nombre = models.CharField(max_length=30)
	provincia = models.CharField(max_length=30)
	canton = models.CharField(max_length=30)
	ciudad = models.CharField(max_length=30)
	telefono = models.CharField(max_length=30)
	celular = models.CharField(max_length=30)






