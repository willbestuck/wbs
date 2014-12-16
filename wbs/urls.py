from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView
from info import views as infoviews

urlpatterns = patterns('',
    # Examples:
    url(r'^$', RedirectView.as_view(url='info/', permanent=False)),
    url(r'^info/', infoviews.index, name='index'), 
    url(r'^about/', infoviews.about, name='about'),
	url(r'^resume/', infoviews.resume, name='resume'),
	url(r'^projects/', infoviews.projects, name='projects'),
	url(r'^contact/', infoviews.contact, name='contact'),
    url(r'^admin/', include(admin.site.urls)),
)
