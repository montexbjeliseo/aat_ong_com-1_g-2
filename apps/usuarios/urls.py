from django.urls import path
from . import views

urlpatterns = [
    path('registro', views.register, name='registro'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('<str:username>/perfil',views.PerfilVista.as_view(),name='perfil'),
]