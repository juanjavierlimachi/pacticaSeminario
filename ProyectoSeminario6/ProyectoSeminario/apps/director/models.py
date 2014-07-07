#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
#import DateTime
# Create your models here.

class Curso(models.Model):
	nombre_Curso=models.CharField(max_length=30)
	def __unicode__(self):
		return self.nombre_Curso

class Alumno(models.Model):
	#usuario=models.ForeignKey(User)
	Nombre_Alumno=models.CharField(max_length=30)
	Apellido_Paterno=models.CharField(max_length=30)
	Apellido_Materno=models.CharField(max_length=30)
	fecha_nacimiento=models.DateField()
	Padre_o_Tutor=models.CharField(max_length=30)
	ci=models.IntegerField(null=False)
	direccion=models.CharField(max_length=50)
	telefono=models.IntegerField(max_length=8)
	fecha_registro = models.DateTimeField(auto_now=True)
	idCurso=models.ForeignKey(Curso)
	class Meta():
		ordering = ['Nombre_Alumno']
	def __unicode__(self):
		return self.Nombre_Alumno

class Materia(models.Model):
	nombre_Materia=models.CharField(max_length=30)
	def __unicode__(self):
		return self.nombre_Materia


class  Materia_Curso(models.Model):
	id_Curso=models.ForeignKey(Curso)
	id_Materia=models.ForeignKey(Materia)

class Profesor(models.Model):
	#usuario=models.ForeignKey(User)
	nombre_Profesor=models.CharField(max_length=30)
	Apellido_Paterno=models.CharField(max_length=30)
	Apellido_Materno=models.CharField(max_length=30)
	ci=models.IntegerField()
	direccion=models.CharField(max_length=50)
	telefono=models.IntegerField()
	fecha_nacimiento=models.DateField()
	fecha_registro = models.DateTimeField(auto_now=True)
	class Meta():
		ordering = ['nombre_Profesor']
	def __unicode__(self):
		return self.nombre_Profesor

class Asignar_Materia(models.Model):
	id_Materia=models.ForeignKey(Materia)
	id_Profesor=models.ForeignKey(Profesor)
	
class AsignarCurso_Profesor(models.Model):
	id_Profesor=models.ForeignKey(Profesor)
	id_Curso=models.ForeignKey(Curso)
	
class director(models.Model):
	nombre=models.CharField(max_length=30)
