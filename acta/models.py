# -*- coding:utf-8 -*-
from django.db import models

from .validators import validate_cedula

# Create your models here.

class Feligres(models.Model):
	SEXO_CHOICES    = (
		('m','Masculino'),('f','Femenino')
		)
	cedula          = models.CharField(max_length=30, help_text='Ingrese un numero de cedula ej:1104688617', unique=True, 
					error_messages  ={'unique': 'Ya existe un feligrés con ese número de cédula'},
					validators=[validate_cedula])
	nombre          = models.CharField(max_length=30,help_text='Ingrese un nombre ej:Jose, Edison')
	apellidos       = models.CharField(max_length=30,help_text='Ingrese apellidos ej: Espinosa, Espinosa Luna')
	lugarNacimiento = models.CharField(max_length=100, verbose_name=u'Lugar de Nacimiento', help_text='Ingrese el lugar de nacimiento');
	fechaNacimiento = models.DateField(verbose_name=u'Fecha de Nacimiento', help_text='Ingrese la Fecha de nacimiento');
	sexo            = models.CharField(max_length=30,choices=SEXO_CHOICES)

	#def __unicode__(self):
	#	return self.nombre

	def __str__(self):
		return self.nombre
	def get_absolute_url(self):
		return "/feligres/%i/" % self.id

class Acta(models.Model):
	numero   = models.CharField(max_length=30)
	feligres =models.ForeignKey(Feligres)
	padrino  = models.CharField(max_length=30)
	madrina  =models.CharField(max_length=30)
	#def __unicode__(self):
	#	return self.numero
	
	def __str__(self):
		return self.numero

class Parroquia(models.Model):
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
							("view_task", "Can see available tasks"),
							("change_task_status", "Can change the status of tasks"),
							("close_task", "Can remove a task by setting its status as closed"),
							('acta.add_parroquia', 'Puede cambiar'),
					  )