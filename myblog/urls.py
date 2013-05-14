from django.conf.urls import patterns, include, url
from blogapp.views import home_page

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^$', main),
    url(r'^', include(admin.site.urls)),
    url(r'^posts$', home_page),
    # Examples:
    #url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^myblog/', include('myblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
