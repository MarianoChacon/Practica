from django.urls import path
from appPracticaClase19 import views

urlpatterns = [
    path('inicio', views.inicio),
    path('cursos', views.cursos),
    path('profesores', views.profesores),
    path('entregables', views.entregables),
    path('estudiante', views.estudiantes),
]