from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='noticias'),
    path('crear/', CrearNoticia.as_view(), name="noticias-crear"),
]