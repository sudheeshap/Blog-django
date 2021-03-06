from django.conf.urls import patterns, include, url
from blogapp.views import *
from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', home_page),
    url(r'^account/login$', login),
    url(r'^account/logout$', logout),
    url(r'^add_post$', add_post),
    url(r'^account/signup$', create_user),
    url(r'^account/check_user$', check_user),
    url(r'^(?P<year>[\d]+)/(?P<month>[\w]+)/(?P<slug>[-\w]+)/$', detail),
    url(r'^add_comment/(\d+)/$', add_comment),
    

    #url(r'^comments/', include('django.contrib.comments.urls')), 
    #url(r'^admin/', include(admin.site.urls)),
    #(r'^(\d+)/$', post),
   
    #url(r'^comments/', include('django.contrib.comments.urls')),
    #url(r"^add_comment/(\d+)/$", add_comment),
    #url(r'^(?P<slug>\d+)/$', include(admin.site.urls)),
    # Examples:
    #url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^myblog/', include('myblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    
)
