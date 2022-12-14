from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from .models import *
from .forms import *

from datetime import datetime

class VerTodasLasNoticias(ListView):
    template_name = 'noticias/noticias.html'
    model = Noticia
    
    def get_context_data(self, **kwargs):                
        ctx = super().get_context_data(**kwargs)
        ctx['noticias'] = Noticia.objects.all()
        if "ordenar_por" in self.request.GET.keys():
            if self.request.GET['ordenar_por'] == "destacadas":
                ctx['noticias'] = Noticia.objects.all().order_by('-visitas')
            elif self.request.GET['ordenar_por'] == "recientes":
                ctx['noticias'] = Noticia.objects.all().order_by('-creado')
        elif "categoria" in self.request.GET.keys():
            ctx['noticias'] = Noticia.objects.filter(categoria_id=self.request.GET['categoria'])
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

class Editar_Noticia(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Noticia
    template_name = 'noticias/editar.html'
    form_class = NuevaNoticiaForm
    def test_func(self):
        return self.request.user.is_superuser

def actualizar_comentario(request, pk, cpk):
    if request.method == "POST":
        form = NuevoComentarioForm(data = request.POST)
        comentario = Comentario.objects.get(pk=cpk)
        if form.is_valid() and comentario.usuario == request.user:
            comentario.texto = form.instance.texto
            comentario.editado = True
            comentario.modificado = datetime.now()
            comentario.save()
        else:
            return redirect('noticias:ver', pk, { 'comment_form': form})
    return redirect('noticias:ver', pk)

def megusta_noticia(request, pk):
    if request.method == "POST":
        noticia = Noticia.objects.get(pk=pk)
        if request.user in noticia.likes.all():
            noticia.likes.remove(request.user)
        else:
            noticia.likes.add(request.user)
        #noticia.save()
    return redirect('noticias:ver', pk)

def megusta_comentario(request, pk, cpk):
    if request.method == "POST":
        comentario = Comentario.objects.get(pk=cpk)
        if request.user in comentario.likes.all():
            comentario.likes.remove(request.user)
        else:
            comentario.likes.add(request.user)
    return redirect('noticias:ver', pk)