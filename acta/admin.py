# -*- coding:utf-8 -*-

from django.contrib import admin
from django.contrib.auth.models import User

from .models import Feligres, Parroquia, Acta, NotaMarginal

class NotaMarginalInline(admin.StackedInline):
	model = NotaMarginal
	extra = 1

class ActaAdmin(admin.ModelAdmin):
	# list_display = ('feligres', 'lugar_celebracion', 'fecha_sacramento')
	# list_filter = ('feligres', 'lugar_celebracion', 'fecha_sacramento')
	inlines = [NotaMarginalInline]
	
	add_fieldsets =  (
		 ('Padres y Padrinos', {
            'classes': ('wide',),
            'fields': ('padrino', 'madrina')}
            ),
        )

	
admin.site.register(Acta, ActaAdmin)
admin.site.register(Feligres)
admin.site.register(Parroquia)