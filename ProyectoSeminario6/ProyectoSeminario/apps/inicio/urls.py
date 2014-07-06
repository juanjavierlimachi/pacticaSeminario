from django.conf.urls import patterns, include, url
from ProyectoSeminario.apps.inicio.views import CrearUsuarios,ingresar,cerrar,verificar,index
urlpatterns = patterns('',
	
    url(r'^$',index),
    url(r'^nuevoUsuario/$', CrearUsuarios),
    url(r'^ingresar/$', ingresar),
    url(r'^cerrar/$', cerrar),
    url(r'^verificar/$',verificar),#verificamos ya el usuario ya existe
)