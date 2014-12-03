import os
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'events.views.index', name='index'),
    url(r'^resources/$', 'resources.views.list_of_resurces', name='list_ofresources'),
    url(r'^resource/add/$', 'resources.views.add_resource', name='add_resource'),
    url(r'^resource/(?P<resource_id>[-\w]+)/$', 'resources.views.edit_resource', name='edit_resource'),
    url(r'^resource/(?P<resource_id>[-\w]+)/del$', 'resources.views.del_resource', name='del_resource'),
    url(r'^resource/(?P<resource_id>[-\w]+)/calendar$', 'resources.views.show_resource_calendar', name='show_resource_calendar'),
    url(r'^resources/out_of_sync$', 'resources.views.out_of_sync', name='resources_out_of_sync'),
    url(r'^resource/(?P<resource_id>[-\w]+)/sync$', 'resources.views.sync', name='sync_resource'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django_cas.views.login'),
    url(r'^accounts/logout/$', 'django_cas.views.logout'),
    url(r'^oauth2callback', 'events.views.auth_return'),

    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': os.path.join(os.path.dirname(__file__), 'static')}),
)
