from django.urls import path
from inicio.views import inicio, crear_servicio, listar_servicios

urlpatterns = [
    path('', inicio, name="inicio"),
    path('crear-servicio/', crear_servicio, name="crear_servicio"),
    path('listar-servicios/', listar_servicios, name="listar_servicios") 
]
