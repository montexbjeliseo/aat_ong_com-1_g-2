from django.urls import path
from .views import *

app_name = 'noticias'

urlpatterns = [
    path('', VerTodasLasNoticias.as_view(), name='index'),
    path('crear/', CrearNoticia.as_view(), name="crear"),
    path('ver/<int:pk>', VerNoticia.as_view(), name='ver'),
    path('categorias', ListaCategoria.as_view(), name='categorias'),
    path('categorias/crear', CrearCategoria.as_view(), name='nueva_categoria'),
    path('ver/<int:pk>/comentar', crear_comentario, name="comentar"),
    path('editar/<int:pk>', Editar_Noticia.as_view(), name='editar'),
    path('ver/<int:pk>/comentar/<int:cpk>/editar', actualizar_comentario, name='editar_comentario'),
    path('ver/<int:pk>/like', megusta_noticia, name='megusta'),
    path('ver/<int:pk>/comentarios/<int:cpk>/like', megusta_comentario, name="megusta_comentario"),
    path('ver/<int:pk>/comentarios/<int:cpk>/borrar', borrar_comentario, name="borrar_comentario")
]