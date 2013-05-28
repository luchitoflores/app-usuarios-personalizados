from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from acta.views import FeligresList, ParroquiaCreate, ParroquiaUpdate, ParroquiaList, ParroquiaDelete

urlpatterns = patterns('acta.views',
	url(r'^feligres/add/$','addFeligres_view', name='addfeligres'),
	# url(r'^feligres/$','feligres_view'),
	url(r'^feligres/$',FeligresList.as_view()),
	url(r'^feligres/ajax/$','feligresajax_view'),
	url(r'^feligres/(?P<pk>\d+)/delete/$','deletefeligres_view',name='eliminarfeligres'),
	url(r'^feligres/(?P<pk>\d+)/$','editfeligres_view',name='editarfeligres'),
	#Urls para administracion de parroquias
	url(r'^parroquia/add$', ParroquiaCreate.as_view(), name='parroquia_create'),
	url(r'^parroquia/(?P<pk>\d+)/$', ParroquiaUpdate.as_view(), name='parroquia_update'),
	url(r'parroquia/(?P<pk>\d+)/delete/$', ParroquiaDelete.as_view(), name='parroquia_delete'), 
	url(r'^parroquia/$', ParroquiaList.as_view(), name='parroquia_list'),
	)

