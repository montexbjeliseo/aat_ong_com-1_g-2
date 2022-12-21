from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as login_user, logout as log_out
from .forms import RegisterUserForm, LoginUserForm
from django.utils.http import url_has_allowed_host_and_scheme
from django.conf import settings
from django.views.generic import DetailView
from os import environ as my_conf
from .models import *
from apps.noticias.models import *
def login(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    ctx = {
        'form': LoginUserForm,
        'categorias': Categoria.objects.all()
    }
    if request.method == "POST":
        form = LoginUserForm(data = request.POST)
        if form.is_valid():
            user = authenticate(username = request.POST['username'], password = request.POST['password'])
            login_user(request, user)
            return redireccion(request)
        else:
            ctx['form'] = form
    
    return render(request, 'usuarios/login.html', ctx)

def register(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    ctx = {
        'form': RegisterUserForm,
        'categorias': Categoria.objects.all()
    }
    if request.method == "POST":
        form = RegisterUserForm(data = request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password1'])
            login_user(request, user)
            return redireccion(request)
        else :
            ctx['form'] = form
    return render(request, 'usuarios/registro.html', ctx)

def logout(request):
    if request.user.is_authenticated:
        log_out(request)
    return redireccion(request)

def redireccion(request):
    nxt = request.GET.get("next", None)
    if nxt is None:
        return redirect(settings.LOGIN_REDIRECT_URL)
    elif my_conf.get('DEBUG'):
        return redirect(nxt)
    elif not url_has_allowed_host_and_scheme(
            url=nxt,
            allowed_hosts={request.get_host()},
            require_https=request.is_secure()):
        return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        return redirect(nxt)

class PerfilVista(DetailView):
    model=Usuario
    template_name='usuarios/perfil.html'
    slug_field = "username"
    slug_url_kwarg = "username"
    context_object_name = 'usuario'
    def get_context_data(self, **kwargs):                
        ctx = super().get_context_data(**kwargs)
        ctx['categorias'] = Categoria.objects.all()
        return ctx
