from django.shortcuts import render
from inicio.models import Servicio

# Create your views here.
def inicio(request):
    return render(request, "inicio/inicio.html")

def crear_servicio(request):
    return render(request, "inicio/crear_servicio.html")