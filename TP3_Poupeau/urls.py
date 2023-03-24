"""TP3_Poupeau URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MiApp.views import (saludar, index, Curso, Alumno, Profesor, buscar_alumno, Agregar_alumno, buscar_profesor,
                          Agregar_profesor, buscar_curso, Agregar_curso)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Bienvenida/', saludar),
    path('',index,name="index"),
    path('Curso/', Curso, name="Curso"),
    path('Alumno/', Alumno, name="Alumno"),
    path('Profesor/', Profesor, name="Profesor"),
    path('Curso/Agregar', Agregar_curso, name="Agregar_curso"),
    path('Alumno/Agregar', Agregar_alumno, name="Agregar_alumno"),
    path('Profesor/Agregar', Agregar_profesor, name="Agregar_profesor"),
    path("Buscar/", buscar_alumno, name = "buscar_alumno"),
    path("Buscar/", buscar_profesor, name= "buscar_profesor"),
    path("Buscar/", buscar_curso, name = "buscar_curso"),
]
