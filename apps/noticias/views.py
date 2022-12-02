from django.shortcuts import render
from .models import *

def index(request):
    ctx = {}
    ctx['samples'] = [1, 2, 3]
    return render(request, 'noticias/noticias.html', ctx)