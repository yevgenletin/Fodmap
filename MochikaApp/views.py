from django.http import HttpResponse
from django.shortcuts import render



# Create your views here.
def home(request):
    return render(request, "MochikaApp/home.html")

def recetas(request):
    return render(request, "MochikaApp/recetas.html")

def tienda(request):
    return render(request, "MochikaApp/tienda.html")

def blog(request):
    return render(request, "MochikaApp/blog.html")

def restaurantes(request):
    return render(request, "MochikaApp/restaurantes.html")

def contacto(request):
    return render(request, "MochikaApp/contacto.html")
