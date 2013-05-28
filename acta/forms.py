#-*- coding: utf-8 -*-
from django.forms import ModelForm 
from django import forms
from acta.models import *
from django.forms.widgets import RadioSelect
from acta.validaciones import *

class FeligresForm(ModelForm):
	# cedula = forms.CharField(error_messages={'required': 'Ingrese un valor para el número de cédula'}, help_text='Ingrese un numero de cedula ej:1104688617')
	
	class Meta():
		model=Feligres
		#widgets = {
         #   'sexo': RadioSelect(),
        #}
		#exclude=('cedula',)
		#fields=('cedula',)

	#crear validaciones personalizadas
	def clean_cedula(self):
		datos=self.cleaned_data['cedula']
		# La sentencia equivalente es igual a la anterior, solo cambio de sintaxis
		#datos=self.cleaned_data.get('cedula')
		if not cedula_valida(datos):
			raise forms.ValidationError('El número de cédula ingresado no es válido')

		return datos
		
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput(render_value=False))





#class FeligresForm(forms.Form):
#	cedula=forms.CharField(max_length=30)	
#	nombre=forms.CharField(max_length=30)
#	apellidos=forms.CharField(max_length=30)
#	sexo=forms.CharField(max_length=30)

