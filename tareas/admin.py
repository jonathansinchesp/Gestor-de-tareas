from django.contrib import admin
from .models import Tarea

# Personalización del admin
class TareaAdmin(admin.ModelAdmin):
    # Campos que se muestran en la lista
    list_display = ('titulo', 'estado', 'fecha_creacion')
    
    # Filtro por estado (barra lateral)
    list_filter = ('estado',)
    
    # Buscador por título
    search_fields = ('titulo', 'descripcion')
    
    # Campos editables directamente en la lista
    list_editable = ('estado',)

# Registra con la personalización
admin.site.register(Tarea, TareaAdmin)