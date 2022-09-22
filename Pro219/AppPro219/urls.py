from django.urls import path
from AppPro219.views import *

urlpatterns = [
    path("", inicio),
    path("cursos/", curso),
    path("profesores/", profesor),
    path("estudiantes/", estudiante),
    path("entregables/", entregable),
]
