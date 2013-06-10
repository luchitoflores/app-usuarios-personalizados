# -*- coding:utf-8 -*-
from django.contrib import admin
# from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from .models import Usuario, PerfilUser
from .forms import UserCreationForm, UserChangeForm


# class PerfilUserInline(admin.StackedInline):
# 	model = PerfilUser
# 	verbose_name_plural = 'Datos de Perfil'

# class UserAdmin(admin.ModelAdmin):
# 	list_display = ('username', 'first_name', 'last_name', 'email')
# 	fields = ('first_name', 'last_name', 'email')
# 	inlines = [PerfilUserInline]

class PerfilUserInline(admin.TabularInline):
    model = PerfilUser

class MyUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('email', 'nombres', 'apellidos', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('is_superuser', 'is_active', 'is_staff')
    fieldsets = (
		(None, {'fields': ('email', 'password')}),
        ('Información Personal', {'fields': ('nombres', 'apellidos', 'cedula', 'lugar_nacimiento', 'fecha_nacimiento', 'sexo')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datos Importantes', {'fields': ('last_login',)}),)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nombres', 'apellidos', 'fecha_nacimiento','password1', 'password2')}
            ),
        )
    search_fields = ('email', 'nombres', 'apellidos')
    ordering = ('nombres', 'apellidos', 'email',)
    filter_horizontal = ('user_permissions',)
    inlines = [PerfilUserInline]

# admin.site.unregister(Group)

# Now register the new UserAdmin...
admin.site.register(Usuario, MyUserAdmin)

# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)