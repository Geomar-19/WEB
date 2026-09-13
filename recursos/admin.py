from django.contrib import admin
from .models import Recurso

@admin.register(Recurso)
class RecursoAdmin(admin.ModelAdmin):
    # Columnas que verás en el panel
    list_display = ('titulo', 'categoria', 'descargas', 'fecha_subida')
    # Filtros laterales
    list_filter = ('categoria', 'fecha_subida')
    # Barra de búsqueda
    search_fields = ('titulo', 'descripcion')
    readonly_fields = ('descargas',) # Para no editar las descargas manualmente por error