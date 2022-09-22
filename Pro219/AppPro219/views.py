from django.shortcuts import render
from django.http import HttpResponse
from AppPro219.models import Curso

def inicio(request):

    return render(request, "AppPro219/inicio.html")

def curso(request):

    cur1 = Curso(nombre="Python", camada=41635)
    cur1.save()

    return HttpResponse(f"El curso que he creado es: {cur1.nombre} y la camada es {cur1.camada}.")


def estudiante(request):

    return render(request, "AppPro219/estudiantes.html")

def profesor(request):

    return render(request, "AppPro219/profesores.html")

def entregable(request):

    return render(request, "AppPro219/entregables.html")