from django.db import models

# Create your models here.
class Servicio(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    tiempo = models.IntegerField()
    descripcion = models.TextField(null=True, blank= True)
    fecha_creacion = models.DateField(null=True)
    imagen = models.ImageField(upload_to='imagenes', null=True, blank=True)
    
    def __str__(self):
        return f'{self.nombre} ${self.precio} ({self.tiempo} min)'