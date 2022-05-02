from django.urls import path
from appPracticaClase19 import views

urlpatterns = [
    path('', views.inicio),
    path('cursos', views.cursos),
    path('profesores', views.profesores),
]