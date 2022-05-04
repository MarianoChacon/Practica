from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request,'appPracticaClase19/incio.html')

def cursos(request):
    return render(request,'appPracticaClase19/cursos.html')

def profesores(request):
    return render(request,'appPracticaClase19/profesores.html')

def estudiantes(request):
    return render(request,'appPracticaClase19/estudiantes.html')

def entregables(request):
    return render(request,'appPracticaClase19/entregables.html')