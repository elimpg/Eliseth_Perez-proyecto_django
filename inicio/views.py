from django.shortcuts import render, redirect
from inicio.models import Servicio
from inicio.forms import CrearServicio, BuscarServicios

# Create your views here.
def inicio(request):
    return render(request, "inicio/inicio.html")

def crear_servicio(request):
    formulario = CrearServicio()
    if request.method == "POST":
        formulario = CrearServicio(request.POST)
        if formulario.is_valid():
            print('Cleaned Data: ', formulario.cleaned_data)
            servicio = Servicio (
                nombre = formulario.cleaned_data.get('nombre'),
                precio = formulario.cleaned_data.get('precio'),
                tiempo = formulario.cleaned_data.get('tiempo'),
                descripcion = formulario.cleaned_data.get('descripcion')
            )
            servicio.save()
            return redirect("listar_servicios")
    
    
    return render(request, 'inicio/crear_servicio.html', {'formulario': formulario})

def listar_servicios(request):
    formulario = BuscarServicios(request.GET)
    if formulario.is_valid():
        nombre = formulario.cleaned_data.get('nombre')
        servicios = Servicio.objects.filter(nombre__icontains=nombre)
        
    return render(request, 'inicio/listar_servicios.html', {'servicios': servicios, 'formulario': formulario})

def detalle_servicio(request, id):
    servicio = Servicio.objects.get(id=id)
    return render(request, 'inicio/detalle_servicio.html', {'servicio': servicio})

def eliminar_servicio(request, id):
    servicio = Servicio.objects.get(id=id)
    servicio.delete()
    return redirect("listar_servicios")