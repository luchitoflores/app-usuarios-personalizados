from django.conf.urls import patterns, include, url
import settings
from django.views.generic import TemplateView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from home.views import GroupCreate, GroupUpdate
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
	url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
	url(r'^$','home.views.index_view'),
	url(r'^',include('acta.urls')),
    url(r'^loginajax/$','home.views.loginajax_view'),
    # url(r'^login/$', 'django.contrib.auth.views.login'),
    # url(r'^login/$', 'home.views.login_view'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', 'home.views.logout_view', name='logoutview'), 
    url(r'^change-password/$', 'home.views.change_password_view', name='change-password'),
    url(r'^about/$', TemplateView.as_view(template_name="about.html")),
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$', TemplateView.as_view(template_name='home.html')),
    url(r'^group/add/$', GroupCreate.as_view(), name='group_create'),
    url(r'^group/$', TemplateView.as_view(template_name='auth/group_list.html'),name='group_list'),
    url(r'^group/(?P<pk>\d+)/$', GroupUpdate.as_view(), name='group_update'),
                 
)
