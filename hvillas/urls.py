from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
                       url(r'^$', 'villas.views.index', name='index'),
                       url(r'^about/$', 'villas.views.about', name='about'),
                       url(r'^contact/$', 'villas.views.contact', name='contact'),
                       url(r'^location/$', 'villas.views.location', name='location'),
                       url(r'^details/$', 'villas.views.details', name='details'),
                       url(r'^resident/$', 'villas.views.resident', name='resident'),
                       url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
                       url(r'^logout/$', 'villas.views.logout_view',name='logout') ,
                    
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
