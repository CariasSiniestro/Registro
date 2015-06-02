from django.conf.urls import patterns, include, url
from django.contrib import admin
from Registro.views import Rifa

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'RegistroCongreso.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^admin/', include(admin.site.urls)),
	url(r'^admin/rifa/', Rifa),
)
