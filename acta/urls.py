from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from .views import (
	FeligresList, ParroquiaCreate, ParroquiaUpdate, ParroquiaList, ParroquiaDelete, ActaList
	)
from django.contrib.auth.decorators import login_required
from .rest import FeligresCreateRead, FeligresCreateReadUpdateDelete


urlpatterns = patterns('acta.views',
	url(r'^acta/$',ActaList.as_view(), name='acta_list'),
	url(r'^feligres/add/$','addFeligres_view', name='addfeligres'),
	# url(r'^feligres/$','feligres_view'),
	url(r'^feligres/$',FeligresList.as_view(), name='feligres_list'),
	url(r'^feligres/ajax/$','feligresajax_view'),
	url(r'^feligres/(?P<pk>\d+)/delete/$','deletefeligres_view',name='eliminarfeligres'),
	url(r'^feligres/(?P<pk>\d+)/$','editfeligres_view',name='editarfeligres'),
	#Urls para administracion de parroquias
	url(r'^parroquia/add$', ParroquiaCreate.as_view(), name='parroquia_create'),
	url(r'^parroquia/(?P<pk>\d+)/$', ParroquiaUpdate.as_view(), name='parroquia_update'),
	url(r'parroquia/(?P<pk>\d+)/delete/$', ParroquiaDelete.as_view(), name='parroquia_delete'), 
	url(r'^parroquia/$', login_required(ParroquiaList.as_view(), login_url='/login/') , name='parroquia_list'),
	url(r'^api/feligres/$', FeligresCreateRead.as_view()),
	url(r'^api/feligres/add$', FeligresCreateReadUpdateDelete.as_view()),
	)

