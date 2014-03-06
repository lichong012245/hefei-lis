from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from dajaxice.core import dajaxice_autodiscover
from django.contrib import admin, auth
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from family.forms import UserCreateForm
from views import UserProfile

dajaxice_autodiscover()
admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^family/', include('family.urls')),
    url(r'^accounts/register/', CreateView.as_view(template_name='registration/register.html',form_class=UserCreateForm,success_url='/'),name='register'),
    url(r'^accounts/profile/', UserProfile,name='profile'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
  
    

    (r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')),
   
     url(r'^admin/', include(admin.site.urls)),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
