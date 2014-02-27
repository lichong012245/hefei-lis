from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from dajaxice.core import dajaxice_autodiscover
from django.contrib import admin

dajaxice_autodiscover()
admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^family/', include('family.urls')),
    

    (r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')),
   
     url(r'^admin/', include(admin.site.urls)),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
