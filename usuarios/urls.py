from django.urls import path
from django.contrib.auth.views import LogoutView
from usuarios.views import login, registrar, ver_perfil, editar_perfil

urlpatterns = [
    path('login/',  login, name='login'),
    path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
    path('registrar/', registrar, name='registrar'),
    path('ver-perfil/', ver_perfil, name='ver_perfil'),
    path('editar-perfil/', editar_perfil, name='editar_perfil')
]