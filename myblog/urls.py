from django.conf.urls import patterns, include, url
from blogapp.views import home_page, detail, add_comment

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^$', home_page),
    # Uncomment the next line to enable the admin:
    url(r'^', include(admin.site.urls)),
    url(r'^posts$', home_page),
    url(r'^posts/(?P<slug>[-\w]+)/$', detail),
    url(r"^add_comment/(\d+)/$", add_comment),
    url(r'^comments/', include('django.contrib.comments.urls')),

    #url(r'^signup$', signup),
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
