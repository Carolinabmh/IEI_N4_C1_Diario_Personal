from django.contrib import admin
from .models import Categoria, Estado, Entrada, HistorialEstado

admin.site.site_header = "Diario Personal"
admin.site.site_title = "Diario Personal"
admin.site.index_title = "Panel de administración"

admin.site.register(Categoria)
admin.site.register(Estado)
@admin.register(Entrada)
class EntradaAdmin(admin.ModelAdmin):
    list_display = (
        'titulo',
        'categoria',
        'estado',
        'usuario',
        'es_publica',
        'fecha_creacion',
    )

    list_filter = (
        'categoria',
        'estado',
        'es_publica',
        'fecha_creacion',
    )

    search_fields = (
        'titulo',
        'contenido',
        'usuario__username',
    )
admin.site.register(HistorialEstado)