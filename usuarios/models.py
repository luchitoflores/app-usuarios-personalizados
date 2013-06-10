# -*- coding:utf-8 -*-

from django.db import models
from django.contrib.auth.models import PermissionsMixin, BaseUserManager, AbstractBaseUser
from django.conf import settings
from iglesia.validators import validate_cedula, validate_date_of_birth


class PerfilUser(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	campo = models.CharField(max_length=200)


class UsuarioManager(BaseUserManager):
	def create_user(self, email, nombres, apellidos, fecha_nacimiento, password=None):
		if not email:
			raise ValueError('Debe proporcionar una dirección de email válida')

		user = self.model(
			email=UsuarioManager.normalize_email(email),
			nombres=nombres, 
			apellidos= apellidos,
			fecha_nacimiento = fecha_nacimiento,
			)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, nombres, apellidos, fecha_nacimiento, password):
		user = self.create_user(email, nombres=nombres, apellidos=apellidos, fecha_nacimiento=fecha_nacimiento, password=password)
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user

class Usuario(AbstractBaseUser, PermissionsMixin):
	
	SEXO_CHOICES    = (
		('m','Masculino'),('f','Femenino')
		)

	email = models.EmailField(unique=True, max_length=225, db_index=True)
	nombres = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=50)
	cedula= models.CharField(max_length=10, validators=[validate_cedula])
	lugar_nacimiento = models.CharField(max_length=30)
	fecha_nacimiento = models.DateField(validators=[validate_date_of_birth])
	sexo            = models.CharField(max_length=30,choices=SEXO_CHOICES)
	is_active = models.BooleanField('El usuario está activo',default=True)
	is_staff = models.BooleanField('Puede entrar al sitio de administración', default=False, help_text='Puede loguearse y entrar a crear objetos')

	objects = UsuarioManager()
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['nombres', 'apellidos', 'fecha_nacimiento']

	def get_full_name(self):
	# The user is identified by their email address
		return '%s %s'  % (self.nombres, self.apellidos)

	def get_short_name(self):
		return self.nombres

	def __unicode__(self):
		return '%s %s'  % (self.nombres, self.apellidos)

	# def has_perm(self, perm, obj=None):
	# 	return True

	# def has_module_perms(self, app_label):
	# 	return True

	# @property
	# def is_staff(self):
	# 	return self.is_admin



