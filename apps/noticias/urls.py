from django.urls import path
from .views import *

app_name = 'noticias'

urlpatterns = [
    path('', VerTodasLasNoticias.as_view(), name='index'),
    path('crear/', CrearNoticia.as_view(), name="crear"),
    path('ver/<int:pk>', VerNoticia.as_view(), name='ver'),
    path('categorias', ListaCategoria.as_view(), name='categorias'),
    path('categorias/crear', CrearCategoria.as_view(), name='nueva_categoria'),
    path('ver/<int:pk>/comentar', crear_comentario, name="comentar")
]