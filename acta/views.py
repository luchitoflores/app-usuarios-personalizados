# -*- coding:utf-8 -*-
# Create your views here.
import json
import logging

from django.shortcuts import render_to_response,render, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from .forms	import *

logger = logging.getLogger(__name__)

def addFeligres_view(request):
	logger.info('entré a añadir feligrés')
	if request.user.is_authenticated():
		if request.method == 'POST':
			form = FeligresForm(request.POST)
			
			if form.is_valid():
				form.save()
				messages.add_message(request, messages.INFO, 'Se añadió con éxito el feligres')
				return HttpResponseRedirect('/feligres')
			else:
				messages.add_message(request, messages.WARNING, 'Uno o más campos son incorrectos')
		else:
			form = FeligresForm()
			
			
		ctx = {'form': form}
		return render(request, 'feligres/addfeligres.html', ctx)
	else:

		return HttpResponseRedirect('/login')


# #esta vista hace búsquedas con peticiones POST
# @login_required(login_url='/login/')
# def feligres_view(request):
# 	if request.method=='POST':
# 		exito = True
# 		criterio=request.POST['criterio']
# 		feligreses=Feligres.objects.filter(Q(nombre__contains=criterio)| Q(apellidos__contains=criterio)
# 			|Q(cedula__contains=criterio)|Q(sexo__contains=criterio))
# 		ctx={'list_feligreses':feligreses, 'exito':exito}
			
# 		return render(request,'feligres/feligres.html',ctx)
# 		# 	return HttpResponse(json.dums({'exito': exito}), mimeType='application/json')


# 	else:
# 		feligreses=Feligres.objects.all().order_by('-cedula')
# 		paginator = Paginator(feligreses, 1)
		
# 		page = request.GET.get('page')

# 		lista = list()

# 		for x in xrange(1,paginator.num_pages):
# 			lista.append(x)


#     	try:
#         	feligreseslist = paginator.page(page)
#         	ctx={'list_feligreses':feligreseslist, 'lista':lista}
#     	except PageNotAnInteger:
#         # If page is not an integer, deliver first page.
#         	feligreseslist = paginator.page(1)
#         	ctx={'list_feligreses':feligreseslist, 'lista':lista}
#     	except EmptyPage:
#     		feligreseslist = paginator.page(paginator.num_pages)
#     		ctx={'list_feligreses':feligreseslist, 'lista':lista}
# 	return render(request,'feligres/feligres.html',ctx)



@login_required(login_url='/login/')
def feligres_view(request):
	logger.info('este es el valor de query antes: '+ request.GET.get('q', 'elida'))
	query = request.GET.get('q', '')	
	logger.info('este es el valor de query despues: '+ query)
	if query:
		logger.info(query)
		qset = (
			Q(nombre__contains=query)| 
			Q(apellidos__contains=query)|
			Q(cedula__contains=query)|
			Q(sexo__contains=query)
		)

		feligreses=Feligres.objects.filter(qset)
		paginator = Paginator(feligreses, 1)
		page = request.GET.get('page')
		lista = list()

		for x in xrange(1,paginator.num_pages):
			lista.append(x)
		try:
			feligreseslist = paginator.page(page)
			ctx={'list_feligreses':feligreseslist, 'lista':lista, 'q':query}
		except PageNotAnInteger:
			feligreseslist = paginator.page(1)
			ctx={'list_feligreses':feligreseslist, 'lista':lista, 'q':query}
		except EmptyPage:
			feligreseslist = paginator.page(paginator.num_pages)
			ctx={'list_feligreses':feligreseslist, 'lista':lista, 'q':query}
		
	else:			
 		feligreses=Feligres.objects.all().order_by('-cedula')
		paginator = Paginator(feligreses, 5)
		page = request.GET.get('page')
		lista = list()

		for x in xrange(1,paginator.num_pages):
			lista.append(x)

    	try:
        	feligreseslist = paginator.page(page)
        	ctx={'list_feligreses':feligreseslist, 'lista':lista}
    	except PageNotAnInteger:
        	feligreseslist = paginator.page(1)
        	ctx={'list_feligreses':feligreseslist, 'lista':lista}
    	except EmptyPage:
    		feligreseslist = paginator.page(paginator.num_pages)
    		ctx={'list_feligreses':feligreseslist, 'lista':lista}
	return render(request,'feligres/feligres.html',ctx)

def editfeligres_view(request,pk):
	fel= get_object_or_404(Feligres, pk=pk)	
	if request.method == 'POST':
		form = FeligresForm(request.POST,instance=fel)
		if form.is_valid():
			form.save()
			messages.add_message(request, messages.SUCCESS, 'Se actualizaron correctamente los datos del feligres '+fel.nombre+' '+fel.apellidos)
			return HttpResponseRedirect('/feligres')

	else:
		form = FeligresForm(instance=fel)
									
	ctx = {'form': form}
	return render(request, 'feligres/editfeligres.html', ctx)

def deletefeligres_view(request,pk):
	context_instance = RequestContext(request)
	fel=Feligres.objects.get(pk=pk)	
	if request.method == 'POST':
		fel.delete()
		messages.add_message(request, messages.WARNING, 'Objeto Eliminado')
		return HttpResponseRedirect('/feligres')

	else:
		form = FeligresForm(instance=fel)
		fel.delete()
		return HttpResponseRedirect('/feligres')
	#ctx = {'form': form}
	#return render_to_response('feligres/deletefeligres.html', ctx, context_instance)




def feligresajax_view(request):
	exito = False
	feligreses=Feligres.objects.all().order_by('-cedula')
	list_feligreses= list()
	for x in feligreses:
		list_feligreses.append({ 'id': x.pk, 'nombre': x.nombre, 'apellidos': x.apellidos})
	ctx={'list_feligreses':list_feligreses, 'exito':exito}
	return HttpResponse(json.dumps(ctx), content_type='application/json')



#Vistas Genéricas 


#Vistas para la clase Parroquia

class ParroquiaList(ListView):
	model                 = Parroquia 
	template_name         = 'parroquia/parroquia_list.html'
	# context_object_name = 'list_parroquia'
	# paginate_by = 5


class ParroquiaCreate(CreateView):
	model               = Parroquia
	template_name       = 'parroquia/parroquia_form.html'
	context_object_name = 'form'
	success_url         = '/parroquia/'
	
	def form_invalid(self, form):
		messages.add_message(self.request, messages.ERROR, 'Datos incorrectos')
		return super(ParroquiaCreate, self).form_invalid(form)

	def form_valid(self, form):
		messages.add_message(self.request, messages.SUCCESS, 'Guardado exitosamente')
		return super(ParroquiaCreate, self).form_valid(form)
	
class ParroquiaUpdate(UpdateView):
	model               = Parroquia 
	template_name       = 'parroquia/parroquia_form.html'
	context_object_name = 'form'
	success_url         = '/parroquia/'

	def form_valid(self, form):
		messages.add_message(self.request, messages.WARNING, 'Objeto Actualizado')
		return super(ParroquiaUpdate, self).form_valid(form)

	def form_invalid(self, form):
		messages.add_message(self.request, messages.ERROR, 'Datos incorrectos')
		return super(ParroquiaUpdate, self).form_invalid(form)


class ParroquiaDelete(DeleteView):
	"""docstring for ParroquiaDelete"""
	model         = Parroquia
	template_name = 'parroquia/parroquia_confirm_delete.html'
	success_url   =  reverse_lazy('parroquia_list')

	def delete(self, request, *args, **kwargs):
		messages.add_message(self.request, messages.ERROR, 'Eliminado Correctamente')
		return super(ParroquiaDelete, self).delete(request, *args, **kwargs)
	
class FeligresList(ListView):
	model = Feligres
	template_name = 'feligres/feligres.html'
	context_object_name = 'list_feligreses'
	paginate_by = '5'



	

			

	