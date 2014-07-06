from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ProyectoSeminario.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #este a la urls del inicio
    url(r'^',include('ProyectoSeminario.apps.inicio.urls')),
    #este a la url de director
    url(r'^',include('ProyectoSeminario.apps.director.urls')),
    #este  es la urls de mi aplicacion profesor
    url(r'^',include('ProyectoSeminario.apps.profesor.urls')),
    #este  es la urls de mi aplicacion alumno
    url(r'^',include('ProyectoSeminario.apps.alumno.urls')),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
        {'document_root':settings.MEDIA_ROOT,}
        ),
)
