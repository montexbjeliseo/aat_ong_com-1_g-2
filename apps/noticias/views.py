from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from .models import *
from .forms import *

class VerTodasLasNoticias(ListView):
    template_name = 'noticias/noticias.html'
    model = Noticia
    
    def get_context_data(self, **kwargs):                
        ctx = super().get_context_data(**kwargs)
        ctx['noticias'] = Noticia.objects.all()
        ctx['categorias'] = Categoria.objects.all()
        return ctx

class CrearNoticia(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    form_class = NuevaNoticiaForm 
    template_name = 'noticias/nueva.html'
    success_url = reverse_lazy('noticias:index')
    
    def test_func(self):
        return self.request.user.is_superuser

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super(CrearNoticia, self).form_valid(form)

class VerNoticia(DetailView):
    model = Noticia
    template_name = 'noticias/_noticia.html'
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        noticia = self.get_object()
        noticia.visitas+=1
        noticia.save()
        ctx['comment_form'] = NuevoComentarioForm()
        return ctx

class ListaCategoria(ListView):
    model = Categoria
    template_name = 'noticias/categorias.html'

class CrearCategoria(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    form_class = NuevaCategoriaForm
    template_name = 'noticias/nueva_categoria.html'
    success_url = reverse_lazy('noticias:categorias')

    def test_func(self):
        return self.request.user.is_superuser

def crear_comentario(request, pk):
    if request.method == "POST":
        form = NuevoComentarioForm(data = request.POST)
        form.instance.usuario = request.user
        noticia = Noticia.objects.get(pk=pk)
        form.instance.noticia = noticia
        if form.is_valid():
            form.save()
        else:
            return redirect('noticias:ver', pk, { 'comment_form': form})
    return redirect('noticias:ver', pk)