from django.urls import path
from .views import *

app_name = 'noticias'

urlpatterns = [
    path('', index, name='index'),
    path('crear/', CrearNoticia.as_view(), name="crear"),
    path('ver/<int:pk>', VerNoticia.as_view(), name='ver'),
]