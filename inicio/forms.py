from django import forms

class CrearServicio(forms.Form):
    nombre = forms.CharField(max_length=50)
    precio = forms.DecimalField(max_digits=8, decimal_places=2)
    tiempo = forms.IntegerField()
    descripcion = forms.CharField(required=False, widget=forms.Textarea)
    
class BuscarServicios(forms.Form):
    nombre = forms.CharField(max_length=50, required=False)