from django.shortcuts import render, render_to_response
from django.http import  HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from ProyectoSeminario.apps.alumno.forms import *
from ProyectoSeminario.apps.director.models import *
from ProyectoSeminario.apps.profesor.models import *
# Create your views here.
def LoginAlumnos(request):
	if request.method=='POST':
		user=request.POST['Nombre']
		p=request.POST['Id']
		print user
		print p
		try:
			u=Alumno.objects.get(Nombre_Alumno=user) #estoy verificando si existe el alumno
			alumno=Alumno.objects.filter(id=p) #optengo en id del Alumno
			curso=Curso.objects.all()
			nota=Notas.objects.all() 
			materias=Materia.objects.all()
			asistencia=Asistencia.objects.all()
			comentario=Comentarios.objects.all()
			profesor=Profesor.objects.all()
			if alumno == p:
				request.session['ci']=u.ci
			return render_to_response('alumno/ingreso.html',{'u':u,'alumno':alumno,'curso':curso,'nota':nota,'materias':materias,'asistencia':asistencia,'comentario':comentario,'profesor':profesor},context_instance=RequestContext(request))
		except Alumno.DoesNotExist:
			#return HttpResponse("datos incorrectos")
			return HttpResponseRedirect('/Error/')
	else:
		formulario=FormLoguin()
	return render_to_response('alumno/loguin.html',{'formulario':formulario}, context_instance=RequestContext(request))