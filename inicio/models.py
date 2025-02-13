from django.db import models

# Create your models here.
class Servicio(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    tiempo = models.IntegerField()
    descripcion = models.TextField(null=True, blank= True)
