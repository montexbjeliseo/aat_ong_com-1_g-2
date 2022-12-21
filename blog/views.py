from urllib import request
from django.shortcuts import render
from apps.noticias.models import Categoria
from apps.slides.models import Slide
from django.views.generic import CreateView
from apps.noticias.models import Noticia
from apps.noticias.forms import NuevoContactoForm
from django.urls import reverse_lazy

def index(request):
    ctx = {
        'ultimas_noticias': list(reversed(Noticia.objects.all())),
        'noticias_destacadas': Noticia.objects.all().order_by('-visitas'),
        'categorias': Categoria.objects.all(),
        'slides': Slide.objects.all(),
    }
    return render(request, 'home.html', ctx)

def about(request):
	return render(request, 'nosotros.html', {'categorias': Categoria.objects.all()})

class ContactoVista(CreateView):
    template_name= 'contacto.html'
    form_class= NuevoContactoForm
    success_url = reverse_lazy('inicio')

    def get_context_data(self, **kwargs):                
        ctx = super().get_context_data(**kwargs)
        ctx['categorias'] = Categoria.objects.all()
        return ctx

def faq(request):
	return render(request, 'nosotros.html', {'categorias': Categoria.objects.all()})
