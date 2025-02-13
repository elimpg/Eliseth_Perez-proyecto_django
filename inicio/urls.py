from django.urls import path
from inicio.views import inicio, crear_servicio

urlpatterns = [
    path('', inicio, name="inicio"),
    path('crear_servicio/', crear_servicio, name="crear_servicio") 
]
