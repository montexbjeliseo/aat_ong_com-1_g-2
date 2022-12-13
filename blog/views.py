from urllib import request
from django.shortcuts import render
from django.views.generic import CreateView
from apps.noticias.models import Noticia
from apps.noticias.forms import NuevoContactoForm
from django.urls import reverse_lazy

def index(request):
    ctx = {
        'noticias': list(reversed(Noticia.objects.all())),
        'categorias': Categoria.objects.all(),
        'slides': Slide.objects.all()
    }
    return render(request, 'home.html', ctx)

def about(request):
	return render(request, 'nosotros.html', {'categorias': Categoria.objects.all()})

class ContactoVista(CreateView):
    template_name= 'contacto.html'
    form_class= NuevoContactoForm
    success_url = reverse_lazy('inicio')

def faq(request):
	return render(request, 'nosotros.html', {'categorias': Categoria.objects.all()})
