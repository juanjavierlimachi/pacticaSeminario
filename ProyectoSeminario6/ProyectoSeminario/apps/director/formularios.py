#from .models import *
from django.contrib import admin
from django.forms import ModelForm
from django import forms
from .models import Alumno, Materia ,Profesor,Curso,Asignar_Materia,Materia_Curso,AsignarCurso_Profesor
from django.contrib.auth.models import User

from django.forms.extras.widgets import SelectDateWidget
class AlumnoForm(forms.ModelForm):
	fecha_nacimiento = forms.DateField(widget=SelectDateWidget(required=False,years=range(1950,2015)),label="fecha nacimiento")
	class Meta():
		model=Alumno

class MatariaForm(ModelForm):
	class Meta():
		model=Materia
class editProForm(ModelForm):
	class Meta():
		model=Profesor
class editCursoForm(ModelForm):
	class Meta():
		model=Curso

class ProfesorForm(forms.Form):
	Nombre=forms.CharField(max_length=30)
	Apellido_Paterno=forms.CharField(max_length=30)
	Apellido_Materno=forms.CharField(max_length=30)
	ci=forms.IntegerField()
	direccion=forms.CharField(max_length=50)
	telefono=forms.IntegerField()
	#exclude=['usuario']

class CursoForm(ModelForm):
	class Meta():
		model=Curso
class MateriasForm(ModelForm): 
	nombre_Materia=forms.CharField(label="Materia")
	class Meta():
		model=Materia

class buscarForm(forms.Form):
	buscar=forms.CharField()

class asignarForm(ModelForm):
	class Meta():
		model=Asignar_Materia
class editAlumForm(ModelForm):
	class Meta():
		model=Alumno
class AsigCursosForm(ModelForm):
	class Meta():
		model=Materia_Curso
class regisArchivoForm(forms.Form):
	csv=forms.FileField()
class CursoProForm(ModelForm):
	class Meta():
		model=AsignarCurso_Profesor

class loguinForm(forms.Form):
    usr=forms.CharField(max_length=30)
    pas=forms.CharField(widget=forms.PasswordInput)
