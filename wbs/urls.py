from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', RedirectView.as_view(url='info/', permanent=False)),
    url(r'^info/', include('info.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
