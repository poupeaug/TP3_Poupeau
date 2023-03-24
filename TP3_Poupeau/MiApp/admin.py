from django.contrib import admin
from MiApp.models import Curso, Profesor, Alumno

admin.site.register(Curso)
admin.site.register(Alumno)
admin.site.register(Profesor)