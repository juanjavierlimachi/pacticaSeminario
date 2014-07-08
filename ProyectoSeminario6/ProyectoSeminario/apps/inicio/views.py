from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from ProyectoSeminario.apps.director.models import Alumno, Profesor,Materia,Curso
# Create your views here.
def index(request):
	return render_to_response('inicio/index.htm',{},context_instance=RequestContext(request))

def CrearUsuarios(request): 
	if request.method=='POST':
		formulario=UserCreationForm(request.POST)
		if formulario.is_valid:
			formulario.save()
			return HttpResponseRedirect('/registrado')
	else:
		formulario=UserCreationForm()
	return render_to_response('inicio/Usernuevo.html',{'formulario':formulario}, context_instance=RequestContext(request))
def verificar(request):  #esta en prueva 
    if request.method=='POST':
        usuario=request.POST['username']
        try:
            u=User.objects.get(username=usuario)
            return HttpResponse("El usuario ya existe")
        except User.DoesNotExist:
            return HttpResponse("Puede usar ese nombre")
    else:
        return HttpResponse()
def ingresar(request):
	if not request.user.is_anonymous():
		return HttpResponseRedirect('/director/') #ingreso director
	if request.method=='POST':
		formulario=AuthenticationForm(request.POST)
		if formulario.is_valid:
			usuario=request.POST['username']
			clave=request.POST['password']
			acceso=authenticate(username=usuario, password=clave)
			if acceso is not None: #este me dirige a la plantilla del director
				if acceso.is_active:
					login(request, acceso)
					return HttpResponseRedirect('/director/')
				else:
					return render_to_response('inicio/noactivo.html',context_instance=RequestContext(request))
			else:
									
				return render_to_response('inicio/nousuario.html',context_instance=RequestContext(request))
	else:
		formulario=AuthenticationForm()
	return render_to_response('inicio/ingresar.html',{'formulario':formulario},context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def privado(request):
	usuario=request.user
	return render_to_response('director/inicio.html',{'usuario':usuario}, context_instance=RequestContext())
#	return HttpResponseRedirect('http://localhost:9595/inicio')
@login_required(login_url='/ingresar')
def cerrar(request):
	logout(request)
	return HttpResponseRedirect('/cerrar/')
