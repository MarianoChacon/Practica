from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return HttpResponse('Vista inicio')

def cursos(request):
    return HttpResponse('Vista cursos')

def profesores(request):
    return HttpResponse('Vista profesores')