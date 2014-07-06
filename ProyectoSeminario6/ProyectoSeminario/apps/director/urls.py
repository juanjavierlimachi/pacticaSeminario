from django.conf.urls import patterns, include, url
from ProyectoSeminario.apps.director.views import *

urlpatterns = patterns('',

    url(r'^inicio/$', inicio),
    url(r'^asingnar/$', AsigMateria),
    url(r'^asingnarCursos/$', asignarCursos),
    
    url(r'^AsignacionExito/$', AsignacionExito),
   url(r'^AsignacionCurso/$', CurosProfesor),
    url(r'^registro/$', RegistrarAlumno),
    url(r'^materias/$', RegistroMateria),
    url(r'^personal/$', RegistroProfesor),
    url(r'^cursos/$', RegistroCurso),
    url(r'^listaMaterias/$', ListarMetarias),
    url(r'^listaCursos/$', listarCurso),
    url(r'^listarProfesores/$', listarProfesores),
    url(r'^exito/$', listarAlumnos),
    url(r'^MateriaPProfesor/(?P<id>\d+)/$',MateriaPProfesor), #este en prueva MateriaPProfesor   dessavilitadoExito
    url(r'^cursoPProfesor/(?P<id>\d+)/$', CursoPProfesor), 
    url(r'^registrado/$', regProExit),
    url(r'^VerAlumnos/(?P<id>\d+)/$',VerAlumnos),
    url(r'^editar/(?P<id>\d+)/$',EditarMateria),
    url(r'^borrar/(?P<id>\d+)/$',EliminarMateria),

    url(r'^editarCurso/(?P<id>\d+)/$',editarCurso),
    url(r'^borrarCurso/(?P<id>\d+)/$',EliminarCurso),
    url(r'^editarP/(?P<id>\d+)/$',editarProfesor),
    url(r'^borrarP/(?P<id>\d+)/$',eliminarP),
    url(r'^editarA/(?P<id>\d+)/$',editarAlumno),
    url(r'^borrarA/(?P<id>\d+)/$',eliminarAlumno),
    url(r'^buscarAlumnos/$', BuscarView.as_view(), name='buscar'),
    url(r'^Materias/(?P<id>\d+)/$',VerMaterias),
    url(r'^dessavilitado/(?P<id>\d+)/$',DesavilitarMateriaCurso),
  #  url(r'^DesCursoPro/(?P<id>\d+)/$',DesCursoPro),  #nueva url desavilitar curso del profesor
    url(r'^Darbaja/$',dessavilitadoExito), #Eli_RelPro_MA desExito
    url(r'^DarbajaMa/(?P<id>\d+)/$',Eli_RelPro_MA),
    url(r'^Darbaj/$',desExito),
    url(r'^archivos/$',regisArchivo),
    url(r'^director/$',base),
    url(r'^validardatos/$', validar), #validar los datos del (a) director

    url(r'^DesCursoPro/(?P<id>\d+)/$',DesCursoPro),  #nueva url desavilitar curso del profesor
    url(r'^buscador/',buscar),
)