from django.urls import path
from inicio.views import inicio, crear_servicio, listar_servicios, detalle_servicio, EditarServicio, EliminarServicio, acerca_de

urlpatterns = [
    path('', inicio, name="inicio"),
    path('crear-servicio/', crear_servicio, name="crear_servicio"),
    path('listar-servicios/', listar_servicios, name="listar_servicios"),
    path('detalle-servicio/<int:id>', detalle_servicio, name="detalle_servicio"),
    # path('eliminar-servicio/<int:id>', eliminar_servicio, name="eliminar_servicio"),
    path('editar-servicio/<int:pk>', EditarServicio.as_view(), name="editar_servicio"),
    path('eliminar-servicio/<int:pk>', EliminarServicio.as_view(), name="eliminar_servicio"),
    path('acerca-del-estudio/', acerca_de, name="acerca_de")
]
