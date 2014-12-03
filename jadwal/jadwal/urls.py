from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'informasi.views.home', name='home'),
    url(r'', include('social_auth.urls')),
    url(r'^logout/$', 'informasi.views.logout', name='logout'),
    url(r'^admin/', include(admin.site.urls)),
)
