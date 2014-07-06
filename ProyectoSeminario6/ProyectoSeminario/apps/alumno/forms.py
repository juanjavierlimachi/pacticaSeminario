from django.contrib import admin
from django.forms import ModelForm
from django import forms
from ProyectoSeminario.apps.director.models import *
#from .models import *
from django.contrib.auth.models import User

class FormLoguin(forms.Form):
    Nombre=forms.CharField(max_length=30)
    Id=forms.CharField(widget=forms.PasswordInput)