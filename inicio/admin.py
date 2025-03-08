from django.contrib import admin
from inicio.models import Servicio
from usuarios.models import InfoExtra

# Register your models here.

admin.site.register(Servicio)
admin.site.register(InfoExtra)
