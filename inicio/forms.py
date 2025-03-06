from django import forms
from inicio.models import Servicio

class CrearServicio(forms.Form):
    nombre = forms.CharField(max_length=50)
    precio = forms.DecimalField(max_digits=8, decimal_places=2)
    tiempo = forms.IntegerField()
    descripcion = forms.CharField(required=False, widget=forms.Textarea)
    fecha_creacion = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    imagen = forms.ImageField(required=False)
    
class BuscarServicios(forms.Form):
    nombre = forms.CharField(max_length=50, required=False)
    
class EditarServicioFormulario(forms.ModelForm):
    fecha_creacion = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Servicio
        fields = '__all__'