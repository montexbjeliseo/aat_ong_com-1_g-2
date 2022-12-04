from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from .models import *
from .forms import *

def index(request):
    ctx = {
        'noticias': list(reversed(Noticia.objects.all()))
    }
    return render(request, 'noticias/noticias.html', ctx)

class CrearNoticia(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    form_class = NuevaNoticiaForm 
    template_name = 'noticias/nueva.html'
    success_url = reverse_lazy('noticias')
    
    def test_func(self):
        return self.request.user.is_superuser
def show(request):
    pass

def edit(request):
    pass

def delete(request):
    pass