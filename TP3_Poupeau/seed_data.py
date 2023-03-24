from MiApp.models import Curso, Alumno, Profesor


for _ in range(0,5):
    Curso(nombre="Nombre de curso", 
    comision="Nombre de comision",
    ).save()

for _ in range(0,5):
    Alumno(nombre ="Nombre", 
    email="Email",
    Dni= "Dni",
    ).save()

for _ in range(0,5):
    Profesor(nombre="Nombre", 
    email ="Email",
    dni="Dni",
    ).save()