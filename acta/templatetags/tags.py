# -*- coding:utf-8 -*-
from django import template
# from acta.views import buscarFeligres
from acta.models import Feligres
from django.http import HttpResponse
import json

register=template.Library()

@register.simple_tag()
def buscar(id):
	feligres = Feligres.objects.get(pk=id)
	return feligres

@register.inclusion_tag('form-search.html', takes_context=True)
def search_tag(context):
    return context

@register.inclusion_tag('messages/messages-info.html', takes_context=True)
def messages_info_tag(context):
    return context

@register.inclusion_tag('messages/messages-warning.html', takes_context=True)
def messages_warning_tag(context):
    return context

@register.inclusion_tag('messages/messages-error.html', takes_context=True)
def messages_error_tag(context):
    return context

@register.inclusion_tag('messages/messages-success.html', takes_context=True)
def messages_success_tag(context):
    return context
	
