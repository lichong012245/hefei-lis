from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from dajaxice.core import dajaxice_autodiscover
from django.contrib import admin, auth
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

dajaxice_autodiscover()
admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^family/', include('family.urls')),
    url(r'^register/', CreateView.as_view(template_name='registration/register.html',form_class=UserCreationForm,success_url='/')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
  
    

    (r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')),
   
     url(r'^admin/', include(admin.site.urls)),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
