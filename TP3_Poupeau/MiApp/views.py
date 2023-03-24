from django.shortcuts import render
from MiApp.models import Alumno, Profesor, Curso
from django.http import HttpResponse
from MiApp.form import AlumnoForm, ProfesorForm, CursoForm

def saludar(request):
    return HttpResponse("Hola bienvenido..")

def index(request):
    return render(request,"MiApp/index.html")

def add_alumno(request):
    context = {
        "form": AlumnoForm(),
        "alumno": Alumno.objects.all(),
        }
    
def Agregar_alumno(request):
    alumno_form = AlumnoForm(request.POST)
    alumno_form.save()
    context = {
        "alumno": Alumno.objects.all(),
        "form": AlumnoForm(),
        }

def buscar_alumno(request):
    criterio = request.GET.get("criterio")
    context = { "alumno": Alumno.objects.filter(nombre__icontains=criterio).all(),
            }
    return render(request, "MiApp/buscar.html", context)

def add_profesor(request):
    context = {
        "form": ProfesorForm(),
        "profesor": Profesor.objects.all(),
        } 
    
def Agregar_profesor(request):
    profesor_form = ProfesorForm(request.POST)
    profesor_form.save()
    context = {
        "profesor": ProfesorForm.objects.all(),
        "form": ProfesorForm(),
        }

def buscar_profesor(request):
    criterio = request.GET.get("criterio")
    context = { "profesor": Profesor.objects.filter(nombre__icontains=criterio).all(),
            }
    return render(request, "MiApp/buscar.html", context)      

def add_curso(request):
    context = {
        "form": CursoForm(),
        "curso": Curso.objects.all(),
        }

def Agregar_curso(request):
    curso_form = CursoForm(request.POST)
    curso_form.save()
    context = {
        "curso": Curso.objects.all(),
        "form": CursoForm(),
        }

def buscar_curso(request):
    criterio = request.GET.get("criterio")
    context = { "curso": Curso.objects.filter(nombre__icontains=criterio).all(),
            }
    return render(request, "MiApp/buscar.html", context)