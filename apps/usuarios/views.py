from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as login_user, logout as log_out
from .forms import RegisterUserForm, LoginUserForm

def login(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    ctx = {
        'form': LoginUserForm
    }
    if request.method == "POST":
        form = LoginUserForm(data = request.POST)
        if form.is_valid():
            user = authenticate(username = request.POST['username'], password = request.POST['password'])
            login_user(request, user)
            return redirect('inicio')
        else:
            return render(request, 'usuarios/login.html', { 'form': form })
    else:
        return render(request, 'usuarios/login.html', ctx)

def register(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    if request.method == "POST":
        form = RegisterUserForm(data = request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password1'])
            login_user(request, user)
            return redirect('inicio')
        else :
            return render(request, 'usuarios/registro.html', { 'form': form })
    else:
        ctx = {
            'form': RegisterUserForm
        }
        return render(request, 'usuarios/registro.html', ctx)

def logout(request):
    if request.user.is_authenticated:
        log_out(request)
    return redirect('inicio')