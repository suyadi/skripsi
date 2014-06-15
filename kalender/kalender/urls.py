import os
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'kegiatan.views.index'),
    url(r'^oauth2callback', 'kegiatan.views.auth_return'),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/login/$', 'django_cas.views.login'),
    url(r'^accounts/logout/$', 'django_cas.views.logout'),

    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': os.path.join(os.path.dirname(__file__), 'static')}),
)
