from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Comentario)
admin.site.register(Contacto)

class Comentarios(admin.TabularInline):
    model = Comentario
    max_num: 0

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'creado')
    inlines = [Comentarios]