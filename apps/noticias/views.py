from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import *
from .forms import *

def index(request):
    ctx = {}
    ctx['samples'] = Noticia.objects.all()
    return render(request, 'noticias/noticias.html', ctx)

class CrearNoticia(LoginRequiredMixin, CreateView):
    form_class = NuevaNoticiaForm 
    template_name = 'noticias/nueva.html'
    success_url = reverse_lazy('noticias')

def show(request):
    pass

def edit(request):
    pass

def delete(request):
    pass