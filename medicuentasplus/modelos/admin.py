from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, HistoriasClinica, Usuario, Ciudad, Especialidad, Cita, Paciente, Consulta
from django.contrib.auth.models import Group

admin.site.unregister(Group)

class CustomUserAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_staff',
        'especialidad', 'departamento'
        )

    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ('especialidad', 'departamento')
        })
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ('especialidad', 'departamento')
        })
    )

class HistoriaClinicaAdmin(admin.ModelAdmin):
    pass

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(HistoriasClinica, HistoriaClinicaAdmin)
admin.site.register(Usuario)
admin.site.register(Ciudad)
admin.site.register(Especialidad)
admin.site.register(Cita)
admin.site.register(Paciente)
admin.site.register(Consulta)

