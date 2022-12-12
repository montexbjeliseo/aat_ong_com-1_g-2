from django.urls import path
from .views import *

app_name = 'slides'

urlpatterns = [
    path('', ListarSlidesVista.as_view(), name="index"),
    path('crear', NuevoSlideVista.as_view(), name="crear_slide"),
]