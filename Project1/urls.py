from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    # Examples:
    url(r'^$', 'Project1.views.home', name='home'),
    url(r'^bio/', 'Project1.views.bio', name='bio'),
    url(r'^disc/', 'Project1.views.disc', name='disc'),
    url(r'^tour/', 'Project1.views.tour', name='tour'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
