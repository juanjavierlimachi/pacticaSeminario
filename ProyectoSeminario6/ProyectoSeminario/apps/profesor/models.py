from django.db import models
from ProyectoSeminario.apps.director.models import *
# Create your models here.    nombre_Curso=models.CharField(max_length=30)
class Asistencia(models.Model):  
	asistencias=models.IntegerField(max_length=1)
	#faltas=models.IntegerField(max_length=1)
	id_Alumno=models.ForeignKey(Alumno)
	id_Profesor=models.ForeignKey(Profesor)
	id_Materia=models.ForeignKey(Materia)
	fecha = models.DateTimeField(auto_now=True)


class Comentarios(models.Model):
	descripcion=models.TextField(max_length=200)
	archivo=models.FileField(upload_to = 'documents')
	Nombre_Profesor=models.ForeignKey(Profesor)
	#url=models.CharField(max_length=200)
	id_curso=models.ForeignKey(Curso)
	fecha=models.DateTimeField(auto_now=True)
	
class Notas(models.Model):
	Bimentre_1=models.IntegerField()
	Bimentre_2=models.IntegerField()
	Bimentre_3=models.IntegerField()
	Bimentre_4=models.IntegerField()  
	nota=models.IntegerField()
	id_Profesor=models.ForeignKey(Profesor)
	id_Alumno=models.ForeignKey(Alumno)
	id_Materia=models.ForeignKey(Materia)
	fecha=models.DateTimeField(auto_now=True)