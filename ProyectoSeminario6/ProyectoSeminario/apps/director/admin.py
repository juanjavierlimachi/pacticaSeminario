from django.contrib import admin
from .models import *


#class AlumnoAdmin(admin.ModelAdmin):
	#list_display=('id','Nombre_Alumno','Apellido_Paterno','Apellido_Materno','Padre_o_Tutor','direccion','idCurso')
	#list_filter=('idCurso',)
	#search_fields=('Curso', 'Alumno__Nombre_alumno')
	#list_aditable=('Nombre_Alumno','Apellido_Paterno','Apellido_Materno','Padre_o_Tutor','direccion','idCurso')

	
#class ProfesoresAdmin(admin.ModelAdmin):
	#list_display=('nombe_Profesor','Apellido_Paterno','Apellido_Materno','ci','direccion')
	#list_filter=('idCurso',)
	#search_fields=('Curso', 'Alumno__Nombre_alumno')
# Register your models here.
#admin.site.register(Alumno,AlumnoAdmin)
admin.site.register(Alumno)
admin.site.register(director)
admin.site.register(Curso)
admin.site.register(Materia)
admin.site.register(Materia_Curso)
admin.site.register(Profesor)
#admin.site.register(Profesor,ProfesoresAdmin)
admin.site.register(Asignar_Materia)
