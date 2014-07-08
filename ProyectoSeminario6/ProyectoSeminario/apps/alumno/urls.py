from django.conf.urls import patterns, include, url
from ProyectoSeminario.apps.alumno.views import *
urlpatterns = patterns('',
    
    url(r'^alumnos/$', LoginAlumnos), 
    url(r'^Cerrarsecion/$', Cerrarsecion), 

)