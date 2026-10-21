from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MiUsuario


@admin.register(MiUsuario)
class MiUsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Información adicional', {
            'fields': (
                'telefono',
                'fecha_nacimiento',
                'biografia',
            )
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Información adicional', {
            'fields': (
                'telefono',
                'fecha_nacimiento',
                'biografia',
            )
        }),
    )

# Register your models here.
