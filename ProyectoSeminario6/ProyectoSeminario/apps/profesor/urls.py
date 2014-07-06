from django.conf.urls import patterns, include, url
from .views import *
urlpatterns = patterns('',

    url(r'^validar/$', validar),
    url(r'^Error/$', Error),
    url(r'^Comentarios/$', RegisComentarios),
    url(r'^guardado/$', guardado),
    url(r'^alumnosDel/(?P<id>\d+)/$',asistenciaCurso),
    url(r'^notas/(?P<id>\d+)/$',NotasCurso),

    url(r'^notasC/(?P<id>\d+)/$',VerNotas),

    url(r'^editarNota/(?P<id>\d+)/$',editarNota),
    url(r'^VerAsistencia/(?P<id>\d+)/$',VerAsistencia),
    url(r'^VerComents/(?P<id>\d+)/$',VerComents),
    url(r'^EditarComentario/(?P<id>\d+)/$',EditarComent),
    url(r'^reportes/(?P<id>\d+)/$',reportes),
   # url(r'^RegAsistencias/$', RegAsistencias), #esta en prueva   EditarComent
    url(r'^eliminarComentario/(?P<id>\d+)/$',EliminarComent),
    url(r'^RegistroAsistencia/$', RegistroAsistencia),
    url(r'^RegistratNotas/$',RegistratNotas),
)