from django.shortcuts import render

def index(request):
    ctx = {}
    ctx['samples'] = [1, 2, 3]
    return render(request, 'home.html', ctx)

def about(request):
	return render(request, 'nosotros.html')

def contact(request):
	return render(request, 'contacto.html')

def faq(request):
	return render(request, 'nosotros.html')