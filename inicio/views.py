from django.shortcuts import render, redirect
from inicio.models import Servicio
from inicio.forms import CrearServicio, BuscarServicios, EditarServicioFormulario
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def inicio(request):
    return render(request, "inicio/inicio.html")

def crear_servicio(request):
    formulario = CrearServicio()
    if request.method == "POST":
        formulario = CrearServicio(request.POST, request.FILES)
        if formulario.is_valid():
            print('Cleaned Data: ', formulario.cleaned_data)
            servicio = Servicio (
                nombre = formulario.cleaned_data.get('nombre'),
                precio = formulario.cleaned_data.get('precio'),
                tiempo = formulario.cleaned_data.get('tiempo'),
                descripcion = formulario.cleaned_data.get('descripcion'),
                fecha_creacion = formulario.cleaned_data.get('fecha_creacion'),
                imagen = formulario.cleaned_data.get('imagen')
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

class EditarServicio(LoginRequiredMixin, UpdateView):
    model = Servicio
    template_name = 'inicio/editar_servicio.html'
    success_url = reverse_lazy("listar_servicios")
    # fields = '__all__'
    form_class = EditarServicioFormulario
    
class EliminarServicio(LoginRequiredMixin, DeleteView):
    model = Servicio
    template_name = 'inicio/eliminar_servicio.html'
    success_url = reverse_lazy("listar_servicios")
    
def acerca_de(request):
    return render(request, "inicio/acerca_de.html")