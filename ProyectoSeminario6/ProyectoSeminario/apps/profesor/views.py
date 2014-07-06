from django.shortcuts import render, render_to_response
from django.http import  HttpResponseRedirect, HttpResponse
from ProyectoSeminario.apps.director.models import *
from ProyectoSeminario.apps.profesor.forms import *
from django.template import RequestContext
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import *
from ProyectoSeminario.settings import RUTA_PROYECTO
import os
import StringIO
from xhtml2pdf import pisa
from django.template.loader import render_to_string
#import datatime
# Create your views here.
def validar(request):
	if request.method=='POST':
		user=request.POST['usr']
		p=request.POST['pas']
		try:
			u=Profesor.objects.get(nombre_Profesor=user) #estoy verificando si existe  de la secretaria
			clave=Profesor.objects.filter(id=p) #optengo en id de la secretaria
			asig=Asignar_Materia.objects.all()
			cursosP=AsignarCurso_Profesor.objects.all() 
			materias=Materia.objects.all()
			#alumnos=Alumno.objects.all()
			cursos=Curso.objects.all()
			if clave == p:
				request.session['ci']=u.ci
			return render_to_response('profesor/ingreso.html',{'u':u,'clave':clave,'asig':asig,'cursosP':cursosP ,'materias':materias,'cursos':cursos},context_instance=RequestContext(request))
		except Profesor.DoesNotExist:
			#return HttpResponse("datos incorrectos")
			return HttpResponseRedirect('/Error/')
	else:
		formulario=loguinForm()
	return render_to_response('profesor/loguin.html',{'formulario':formulario}, context_instance=RequestContext(request))


def Error(request):
	return render_to_response('profesor/Error.html',{}, context_instance=RequestContext(request))
def misMaterias(request,id):
	#p=request.POST['pas']
	profesores=Profesor.objects.filter(id=id)
	a=Asignar_Materia.objects.filter(id_Profesor_id=id)
	m=Materia.objects.all()
	return render_to_response('profesor/misMaterias.html',{'a':a,'m':m}, context_instance=RequestContext(request))

def asistenciaCurso(request,id):
	alumno=Alumno.objects.filter(idCurso_id=id)
	curso=Curso.objects.get(id=id)
	return render_to_response('profesor/asistencia.html',{'alumno':alumno,'curso':curso}, context_instance=RequestContext(request))
def NotasCurso(request,id):
	alumno=Alumno.objects.filter(idCurso_id=id)
	curso=Curso.objects.get(id=id)
	return render_to_response('profesor/RegisNotas.html',{'alumno':alumno,'curso':curso}, context_instance=RequestContext(request))
def guardado(request):
	return render_to_response('profesor/guardado.html',{}, context_instance=RequestContext(request))


def RegisComentarios(request):
	if request.method=='POST':
		formulario=comentarioForm(request.POST, request.FILES)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/guardado/')
	else:
		formulario=comentarioForm()
	return render_to_response('profesor/Comentarios.html',{'formulario':formulario},context_instance=RequestContext(request))

"""def RegAsistencias(request):
	if request.method=='POST':
		formulario=RegistrosForm(request.POST)
		#u=request.POST['usr']
		if formulario.is_valid():
			a=Asistencia()
			a.asistencias=request.POST['asistencias']
			a.faltas=request.POST['faltas']
			a.id_Alumno=request.POST['id_Alumno']
			a.id_Profesor=request.POST['id_Profesor']
			#formulario.save()
			a.save()
			return HttpResponseRedirect('/guardado/')
	else:
		formulario=RegistrosForm()
		return ender_to_response('profesor/asistencia.html',{'formulario':formulario}, context_instance=RequestContext(request))"""
def VerNotas(request,id):
	alumno=Alumno.objects.filter(idCurso_id=id)
	curso=Curso.objects.get(id=id)
	nota=Notas.objects.all()
	materia=Materia.objects.all()
	return render_to_response('profesor/notas.html',{'alumno':alumno,'curso':curso,'nota':nota,'materia':materia}, context_instance=RequestContext(request))
def editarNota(request,id):
	nota=Notas.objects.get(id=id)
	if request.method=='POST':
		formulario=NotasForm(request.POST, instance=nota)
		if formulario.is_valid():
			n=formulario.save()
			n.save()
			return HttpResponseRedirect('/notasC/1/')
	else:
		formulario=NotasForm(instance=nota)
	return render_to_response('profesor/EditarNotas.html',{'formulario':formulario}, RequestContext(request))
def VerAsistencia(request,id):
	alumno=Alumno.objects.filter(idCurso_id=id)
	curso=Curso.objects.get(id=id)
	asistencia=Asistencia.objects.all()
	return render_to_response('profesor/VerAsistencia.html',{'curso':curso,'alumno':alumno,'asistencia':asistencia},context_instance=RequestContext(request))
def VerComents(request,id):
	curso=Curso.objects.filter(id=id)
	comentario=Comentarios.objects.all()
	return render_to_response('profesor/VerComents.html',{'comentario':comentario,'curso':curso},context_instance=RequestContext(request))

def reportes(request,id): #ya es filtrando los alumnos por curso
	curso=Curso.objects.filter(id=id)
	alum=Alumno.objects.filter(idCurso_id=id)
	html=render_to_string("profesor/reporteAlum.html",{'pagesiza':'A4','alum':alum,'curso':curso},context_instance=RequestContext(request))
	return generar_pdf(html)

def generar_pdf(html):
	resultado=StringIO.StringIO()
	pdf=pisa.pisaDocument(StringIO.StringIO(html.encode("UTF:8")),resultado)
	if not pdf.err:
		return HttpResponse(resultado.getvalue(),mimetype='application/pdf')
	return HttpResponse("error al generar el archivo")

def EditarComent(request,id): #nueva funcion 
	comentario=Comentarios.objects.get(id=id)
	if request.method=='POST':
		formulario=FormComentarios(request.POST, instance=comentario)
		if formulario.is_valid():
			c=formulario.save()
			c.save()
			return HttpResponseRedirect('//')
	else:
		formulario=FormComentarios(instance=comentario)
	return render_to_response('profesor/editComentario.html',{'formulario':formulario},RequestContext(request))

def EliminarComent(request,id):
	comentario=Comentarios.objects.get(id=id)
	comentario.delete()
	return HttpResponseRedirect('/VerComents/1/')
#def EditarAsistencia(request):
def RegistroAsistencia(request):
	if request.method=='POST':
		formulario=FormAsistencia(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('//')
	else:
		formulario=FormAsistencia()
	return render_to_response('profesor/RegistroAsistencia.html',{'formulario':formulario}, context_instance=RequestContext(request))
def RegistratNotas(request):
	if request.method=='POST':
		formulario=FormNotas(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('//')
	else:
		formulario=FormNotas()
	return render_to_response('profesor/RegistratNotas.html',{'formulario':formulario}, context_instance=RequestContext(request))