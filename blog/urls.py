from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

from apps.noticias.models import Contacto
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='inicio'),
    path('nosotros', views.about, name='nosotros'),
    path('contacto', views.ContactoVista.as_view(), name='contacto'),
    path('faq', views.faq, 'faq'),
    path('noticias/', include('apps.noticias.urls')),
    path('usuarios/', include('apps.usuarios.urls')),
    path('slides/', include('apps.slides.urls')),
]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT})
]