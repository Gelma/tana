from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'aeroplanisti.views.home', name='home'),
#    url(r'^login/$', 'aeroplanisti.views.login', name='login'),
#    url(r'^logout/$', 'aeroplanisti.views.logout', name='logout'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
