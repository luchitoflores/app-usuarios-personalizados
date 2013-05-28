# *-* coding:utf-8 *-* 
# Create your views here.
from django.shortcuts import render_to_response, render
import json
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def index_view(request):
	return render_to_response('index.html')


def loginajax_view(request):	
	if request.method == 'POST':
		exito = False
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None and user.is_active:
			login(request,user)
			exito = True
			# return HttpResponseRedirect('/')
			ctx = {'exito': exito}
			return HttpResponse(json.dumps(ctx), content_type='application/json')

		else:
			ctx = {'exito': exito}
			return HttpResponse(json.dumps(ctx), content_type='application/json')


	else:
		exito = False
		ctx = json.dumps({'exito': exito})
		return HttpResponse(ctx, content_type="application/json; charset=uft8")

#Login de usuarios sin utilizar ningún formulario preestablecido
# def login_view(request):
# 	if request.user.is_authenticated():
# 		return HttpResponseRedirect('/feligres/add')
# 	else:
# 		if request.method == 'POST':
# 			username = request.POST['username']
# 			password = request.POST['password']
# 			user = authenticate(username=username, password=password)
# 			if user is not None and user.is_active:
# 				login(request,user)
# 				return HttpResponseRedirect('/')
# 			else:
# 				messages.add_message(request, messages.ERROR, 'El user o la pass son incorrectas')
# 		return render(request, 'login.html')


#Login con AthenticateForm	
def login_view(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		if request.method == 'POST':		
			form = AuthenticationForm(data=request.POST)
			if form.is_valid():
				username = request.POST['username']
				password = request.POST['password']
				user = authenticate(username=username, password=password)

				if user is not None and user.is_active:
					login(request, user)
					return HttpResponseRedirect('/')
				else:
					messages.add_message(request, messages.ERROR, 'El user is None')
			else:
				messages.add_message(request, messages.ERROR, 'El form no es válido')
		else:
			form = AuthenticationForm()
	return render(request, 'login.html', {'form':form})


def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

##Cambiar la contraseña sin proporcionar la antigua contraseña
# @login_required(login_url='/login/')
# def change_password_view(request):
# 	user = request.user
# 	if request.method == 'POST':
# 		form = SetPasswordForm(user, request.POST)
# 		if form.is_valid():
# 			form.save()
# 			logout(request)
# 			messages.add_message(request, messages.INFO, 'El cambio de clave se realizó con éxito')
# 			return HttpResponseRedirect('/')
# 		else:
# 			messages.add_message(request, messages.ERROR, 'Los datos ingresados no son válidos')
# 	else:
# 		form = SetPasswordForm(user)

# 	ctx = {'form': form}
# 	return render(request, 'change-password.html', ctx)
# 	

#Cambiar la contraseña proporcionando la antigua contraseña 
@login_required(login_url='/login/')
def change_password_view(request):
	user = request.user
	if request.method == 'POST':
		form = PasswordChangeForm(user, request.POST)
		if form.is_valid():
			form.save()
			logout(request)
			messages.add_message(request, messages.INFO, 'El cambio de clave se realizó con éxito')
			return HttpResponseRedirect('/')
		else:
			messages.add_message(request, messages.ERROR, 'Revise los errores')
	else:
		form = PasswordChangeForm(user)

	ctx = {'form': form}
	return render(request, 'change-password.html', ctx)
	

