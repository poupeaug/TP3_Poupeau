from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    comision = models.IntegerField()

    def __str__(self):
        return f"""Datos del Curso: 
        Nombre: {self.nombre}  
        Comision:{self.comision}""" 
        

class Alumno(models.Model):
    nombre = models.CharField(max_length=40)
    email = models.EmailField(max_length=60)
    dni = models.IntegerField()

    def __str__(self):
        return f"""Datos del Alumno: 
        Nombre: {self.nombre}  
        Email:{self.email} 
        Dni: {self.dni}""" 


class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    email = models.EmailField(max_length=60)
    dni = models.IntegerField()

    def __str__(self):
        return f"""Datos del Profesor: 
        Nombre: {self.nombre}  
        Email:{self.email} 
        Dni: {self.dni}""" 
        