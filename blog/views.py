from django.shortcuts import render
from apps.noticias.models import *
from apps.slides.models import Slide

def index(request):
    ctx = {
        'noticias': list(reversed(Noticia.objects.all())),
        'categorias': Categoria.objects.all(),
        'slides': Slide.objects.all()
    }
    return render(request, 'home.html', ctx)

def about(request):
	return render(request, 'nosotros.html')

def contact(request):
	return render(request, 'contacto.html')

def faq(request):
	return render(request, 'nosotros.html')
