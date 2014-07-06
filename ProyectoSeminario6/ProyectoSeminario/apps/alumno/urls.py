from django.conf.urls import patterns, include, url
from ProyectoSeminario.apps.alumno.views import LoginAlumnos
urlpatterns = patterns('',
    
    url(r'^alumnos/$', LoginAlumnos),#verificamos ya el usuario ya existe
)