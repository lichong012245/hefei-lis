from django.conf.urls import patterns, include, url
#from family.views import Profile

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^family/member/(?P<slug>\w+)/$', 'lis.views.Profile', name='profile'),
    # url(r'^lis/', include('lis.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
