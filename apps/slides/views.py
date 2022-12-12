from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .forms import *
from .models import *

class NuevoSlideVista(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    form_class = NuevoSlideFormulario
    template_name = 'slides/nuevo.html'
    success_url = reverse_lazy('slides:index')
    def test_func(self):
        return self.request.user.is_superuser

class ListarSlidesVista(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Slide
    template_name = 'slides/slides.html'
    def test_func(self):
        return self.request.user.is_superuser