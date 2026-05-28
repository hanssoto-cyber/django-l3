from django.contrib import admin
from .models import Articulo


@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_publicacion', 'publicado')
    list_filter = ('publicado', 'fecha_publicacion')
    search_fields = ('titulo', 'contenido')
    prepopulated_fields = {'slug': ('titulo',)}
    list_editable = ('publicado',)