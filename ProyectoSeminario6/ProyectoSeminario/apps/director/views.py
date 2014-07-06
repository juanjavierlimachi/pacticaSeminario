from django.shortcuts import render, render_to_response
from django.http import  HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from .formularios import  AlumnoForm,MatariaForm,ProfesorForm,CursoForm,MateriasForm,buscarForm,asignarForm,editProForm,editCursoForm,editAlumForm,AsigCursosForm,regisArchivoForm,CursoProForm,loguinForm
from .models import *
# Create your views here.
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from ProyectoSeminario.settings import RUTA_PROYECTO
import json
import pdb
import os
import csv
import datetime

from django.views.generic import TemplateView
def inicio(request):
	
	#return render_to_response('profesorIndex.html')
	return render_to_response('director/inicio.html')
def base(request):
	return render_to_response('base.html')

def AsignacionExito(request):
	return render_to_response('director/Asig_exito.html',{},context_instance=RequestContext(request))

def CurosProfesor(request):
	if request.method=='POST':
		formulario=CursoProForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/AsignacionExito/')
	else:
		formulario=CursoProForm()
	return render_to_response('director/CursoProfesor.html',{'formulario':formulario}, context_instance=RequestContext(request))
def regProExit(request):
	return render_to_response('director/ReExito.html',{},context_instance=RequestContext(request))
def RegistroMateria(request):
	if request.method=='POST':
		formu=MatariaForm(request.POST)
		if formu.is_valid():
			formu.save()
			return HttpResponseRedirect('/listaMaterias/')
	else:
		formu=MatariaForm()
	return render_to_response('director/RegistroMateria.html',{'formu':formu},context_instance=RequestContext(request))
def ListarMetarias(request):
	materias=Materia.objects.all()
	return render_to_response('director/materias.html',{'materias':materias}, context_instance=RequestContext(request))

def listarProfesores(request):
	profesores=Profesor.objects.all()
	return render_to_response('director/profesores.html',{'profesores':profesores}, context_instance=RequestContext(request))
def EditarMateria(request,id):
	materia=Materia.objects.get(id=id)
	#formulario=MateriasForm(request.POST.copy(), instance=materia)
	if request.method=='POST':
		formulario=MateriasForm(request.POST, instance=materia)
		if formulario.is_valid():
			f=formulario.save()
			f.save()
			return HttpResponseRedirect('/listaMaterias/')
	else:
		formulario=MateriasForm(instance=materia)
	return render_to_response('director/editarM.html',{'formulario':formulario}, RequestContext(request))

def editarCurso(request,id):
	curso=Curso.objects.get(id=id)
	if request.method=='POST':
		formulario=editCursoForm(request.POST, instance=curso)
		if formulario.is_valid():
			c=formulario.save()
			c.save()
			return HttpResponseRedirect('/listaCursos/')
	else:
		formulario=editCursoForm(instance=curso)
	return render_to_response('director/editarCurso.html',{'formulario':formulario}, RequestContext(request))

def editarProfesor(request,id):
	profesor=Profesor.objects.get(id=id)
	if request.method=='POST':
		formulario=editProForm(request.POST,instance=profesor)
		if formulario.is_valid():
			p=formulario.save()
			p.save()
			return HttpResponseRedirect('/listarProfesores/')
	else:
		formulario=editProForm(instance=profesor)
	return render_to_response('director/editarP.html',{'formulario':formulario}, RequestContext(request))
def editarAlumno(request,id):
	alumno=Alumno.objects.get(id=id)
	if request.method=='POST':
		formulario=editAlumForm(request.POST,instance=alumno)
		if formulario.is_valid():
			a=formulario.save()
			a.save()
			return HttpResponseRedirect('/exito/')
	else:
		formulario=editAlumForm(instance=alumno)
	return render_to_response('director/editarA.html',{'formulario':formulario},RequestContext(request))

def eliminarP(request,id):
	pro=Profesor.objects.get(id=id)
	pro.delete()
	return HttpResponseRedirect('/listarProfesores/')

def eliminarAlumno(request,id):#este metodo esta incompleto
	eli=Alumno.objects.get(id=id)
	eli.delete()
	return HttpResponseRedirect('/exito/')

def EliminarMateria(request,id):
	eli=Materia.objects.get(id=id)
	eli.delete()
	return HttpResponseRedirect('/listaMaterias/')
def EliminarCurso(request,id):
	cu=Curso.objects.get(id=id)
	cu.delete()
	return HttpResponseRedirect('/listaCursos/')

def listarAlumnos(request):
	alumno=Alumno.objects.all()
	return render_to_response('director/listaAlumnos.html',{'alumno':alumno},context_instance=RequestContext(request))

def RegistrarAlumno(request):
	if request.method=='POST':
		formulario=AlumnoForm(request.POST)
		if formulario.is_valid():
			alumno=Alumno()
			alumno.Nombre_Alumno=request.POST['Nombre']
			alumno.Apellido_Paterno=request.POST['Apellido_Paterno']
			alumno.Apellido_Materno=request.POST['Apellido_Materno']
			alumno.Padre_o_Tutor=request.POST['Padre_o_Tutor']
			alumno.ci=request.POST['ci']
			alumno.direccion=request.POST['direccion']
			alumno.telefono=request.POST['telefono']
			anio=request.POST['sanio']
			mes=request.POST['smes']
			dia=request.POST['sdia']
			alumno.fecha_nacimiento=anio+"-"+mes+"-"+dia
			alumno.idCurso_id=request.POST['idCurso']
			alumno.save()
			return HttpResponseRedirect('/exito/')
	else:
		formulario=AlumnoForm()
	listadia=range(1,32)
	listames=range(1,13)
	listaanio=range(2014,1950,-1)
	return render_to_response('director/registro.html',{'formulario':formulario,'listadia':listadia,'listames':listames,'listaanio':listaanio}, context_instance=RequestContext(request))
def RegistroProfesor(request):
	if request.method=='POST':
		formulario=ProfesorForm(request.POST)
		if formulario.is_valid():
			profe=Profesor()
			profe.nombre_Profesor=request.POST['Nombre']
			profe.Apellido_Paterno=request.POST['Apellido_Paterno']
			profe.Apellido_Materno=request.POST['Apellido_Materno']
			profe.ci=request.POST['ci']
			profe.direccion=request.POST['direccion']
			profe.telefono=request.POST['telefono']
			anio=request.POST['sanio']
			mes=request.POST['smes']
			dia=request.POST['sdia']
			profe.fecha_nacimiento=anio+"-"+mes+"-"+dia
			#formulario.save()
			profe.save()
			#profesor=Profesor.objects.create(nombre_Profesor=nombre,Apellido_Paterno=apellidop,Apellido_Materno=apellidom,ci=ci,direccion=direccion,telefono=telf,fecha_nacimiento=fecha)
			return HttpResponseRedirect('/registrado/')
	else:
		formulario=ProfesorForm()
	listadia=range(1,32)
	listames=range(1,13)
	listaanio=range(2014,1950,-1)
	return render_to_response('director/RegisPersonal.html',{'formulario':formulario,'listaanio':listaanio,'listames':listames,'listadia':listadia}, context_instance=RequestContext(request))


def RegistroCurso(request):
	if request.method=='POST':
		formulario=CursoForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/listaCursos/')
	else:
		formulario=CursoForm()
	return render_to_response('director/registroCurso.html',{'formulario':formulario}, context_instance=RequestContext(request))

def listarCurso(request):
	cursos=Curso.objects.all()
	return render_to_response('director/listarCurso.html',{'cursos':cursos},context_instance=RequestContext(request))


def buscar(request):
	if request.method=='POST':
		formulario=buscarForm(request.POST)
		if (formulario.is_valid()):
			criterio=request.POST["buscar"]
			lista=Alumno.objects.filter(Q(Nombre_Alumno__contains=criterio) or Q(Apellido_Paterno__contains=criterio))
			return render_to_response('director/resultadoBus.html',{'lista':lista},RequestContext(request))
	formulario=buscarForm()
	return render_to_response('director/buscador.html',{'formulario':formulario},RequestContext(request))

def AsigMateria(request):
	if request.method=='POST':
		formulario=asignarForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/AsignacionExito/')
	else:
		formulario=asignarForm()
	return render_to_response('director/AsigMateria.html',{'formulario':formulario}, context_instance=RequestContext(request))

class BuscarView(TemplateView):
	
	def post(self,request,*args, **kwargs):
		buscar=request.POST['buscalo']
		alumnos=Alumno.objects.filter(Nombre_Alumno__contains=buscar)
		if alumnos:
			print "ha preguntado por un alumno"
		else:
			profesor=Profesor.objects.filter(nombre_Profesor__contains=buscar)
			#print profesor
		return render(request, 'director/buscarA.html',{'alumnos':alumnos, 'alumno':True},context_instance=RequestContext(request))  #alumnos es mi clave iterador

def MateriaPProfesor(request,id):
	Amaterias=Asignar_Materia.objects.all()
	profesor=Profesor.objects.filter(id=id)  #sola mente estoy assiendo conoser el id k le estoy mandando
	materia=Materia.objects.all()
	return render_to_response('director/maPProfesor.html',{'Amaterias':Amaterias,'materia':materia,'profesor':profesor},context_instance=RequestContext(request))
def CursoPProfesor(request,id):
	cursosPro=AsignarCurso_Profesor.objects.all()
	profesor=Profesor.objects.filter(id=id)
	cursos=Curso.objects.all()
	return render_to_response('director/CursoPProfesor.html',{'cursosPro':cursosPro,'profesor':profesor,'cursos':cursos}, context_instance=RequestContext(request))
def VerAlumnos(request,id): # para ver los alumnos por curso
	curso=Curso.objects.filter(id=id)
	alumnos=Alumno.objects.all()
	return render_to_response('director/VerAlumnos.html',{'alumnos':alumnos,'curso':curso},context_instance=RequestContext(request))
def asignarCursos(request):
	if request.method=='POST':
		formulario=AsigCursosForm(request.POST)
		if formulario.is_valid():
			estado=False
			formulario.save()
			return HttpResponseRedirect('/AsignacionExito/')
	else:
		formulario=AsigCursosForm()
	estado=True
	return render_to_response('director/asignarCursos.html',{'formulario':formulario,'estado':estado}, context_instance=RequestContext(request))

def VerMaterias(request,id):
	materia=Materia_Curso.objects.all()
	curso=Curso.objects.filter(id=id)
	mat=Materia.objects.all()
	return render_to_response('director/materiasC.html',{'materia':materia,'curso':curso,'mat':mat}, context_instance=RequestContext(request))
def DesavilitarMateriaCurso(request,id):
	materia=Materia_Curso.objects.get(id=id)
	materia.delete()
	return HttpResponseRedirect('/Darbaja/')

def dessavilitadoExito(request): #estmos dando un mensaje de exito sise ha desavilitado la materia de curso
	materia=Materia.objects.all()
	curso=Curso.objects.all()
	return render_to_response('director/desExito.html',{'materia':materia,'curso':curso},context_instance=RequestContext(request))

def Eli_RelPro_MA(request,id): #estamos dando de daja profesor
	a=Asignar_Materia.objects.get(id=id)
	a.delete()
	return HttpResponseRedirect('/Darbaj/')
def desExito(request):
	profe=Profesor.objects.all()
	materia=Materia.objects.all()
	return render_to_response('director/desExitoPro.html',{'profe':profe,'materia':materia}, context_instance=RequestContext(request))

def regisArchivo(request):
	if request.method=='POST':
		formulario=regisArchivoForm(request.POST,request.FILES)
		if formulario.is_valid():
			destino=open(os.path.join(RUTA_PROYECTO,"archivos/datos.csv"),"wb+")
			archi=request.FILES["csv"]
			for info in archi.chunks():
				destino.write(info)
			destino.close()
			leerarchi=csv.reader(open(os.path.join(RUTA_PROYECTO,"archivos/datos.csv"),"rb"))
			for index,row in enumerate(leerarchi):
				es=Alumno()
				#if row[0]!="":
				es.Nombre_Alumno=row[0]
				es.Apellido_Paterno=row[1]
				es.Apellido_Materno=row[2]
				es.fecha_nacimiento=datetime.datetime.strptime(row[3],"%Y-%m-%d").date()
				es.Padre_o_Tutor=row[4]
				es.ci=row[5]
				es.direccion=row[6]
				es.telefono=row[7]
				es.idCurso_id=int(row[8])
				es.save()
			request.session["success"]=True
			return HttpResponseRedirect("/exito/")
	else:
		formulario=regisArchivoForm()
	return render_to_response('director/subir.html',{'formulario':formulario},context_instance=RequestContext(request))

def validar(request):
	if request.method=='POST':
		user=request.POST['usr']
		p=request.POST['pas']
		try:
			u=director.objects.get(nombre=user) #estoy verificando si existe el profesor
			clave=director.objects.filter(id=p) #optengo en id del profesor
			if clave == p:
				request.session['nombre']=clave.id
			return render_to_response('base.html',{'u':u},context_instance=RequestContext(request))
		except director.DoesNotExist:
			#return HttpResponse("datos incorrectos")
			return HttpResponseRedirect('/Error/')
	else:
		formulario=loguinForm()
	return render_to_response('director/logeo.html',{'formulario':formulario}, context_instance=RequestContext(request))

def DesCursoPro(request,id): #estmos dessabilitando el curso del profesorrrrrrr
	a=AsignarCurso_Profesor.objects.get(id=id)
	a.delete()
	return HttpResponseRedirect('/Darbaja/')