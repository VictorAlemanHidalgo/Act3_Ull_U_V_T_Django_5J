from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("Administradores/", views.Administradores, name="Administradores"),
    path("Afiliados/", views.Afiliados, name="Afiliados"),
    path("Servicios/", views.Servicios, name="Servicios"),
    path("Productos/", views.Productos, name="Productos"),
]
