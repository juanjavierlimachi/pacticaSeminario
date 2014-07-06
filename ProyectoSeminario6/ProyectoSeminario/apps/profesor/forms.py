from django.contrib import admin
from django.forms import ModelForm
from django import forms
from ProyectoSeminario.apps.director.models import Profesor
from .models import *
from django.contrib.auth.models import User

class loguinForm(forms.Form):
    usr=forms.CharField(max_length=30)
    pas=forms.CharField(widget=forms.PasswordInput)

class comentarioForm(ModelForm):
	class Meta():
		model=Comentarios
class NotasForm(ModelForm):
	class Meta():
		model=Notas
#class RegistrosForm(ModelForm): 
#	class Meta():
#		model=registro
class FormComentarios(ModelForm):##este es una formulario de editar comentarios
	class Meta():
		model=Comentarios

class FormAsistencia(ModelForm):
	class Meta():
		model=Asistencia
class FormNotas(ModelForm):
	class Meta():
		model=Notas