from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from dajaxice.core import dajaxice_autodiscover
from django.contrib import admin, auth
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from family.forms import UserCreateForm
from views import UserProfile, Index,Contact,Gallery,ShowArticle
from django.core.urlresolvers import reverse_lazy

dajaxice_autodiscover()
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',Index, name='index'),
    url(r'^gallery/$',Gallery, name='gallery'),
    url(r'^family/', include('family.urls')),
    url(r'^accounts/register/$', CreateView.as_view(template_name='registration/register.html',form_class=UserCreateForm,success_url=reverse_lazy('index')),name='register'),
    url(r'^accounts/profile/$', UserProfile,name='profile'),
    url(r'^accounts/logout/$','django.contrib.auth.views.logout',{'next_page':'/'}),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^contact/$', Contact, name='contact'),
    url(r'^article/$', ShowArticle, name='article'),
  
    

    (r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')),
   
     url(r'^admin/', include(admin.site.urls)),

)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
