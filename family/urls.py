from django.conf.urls import patterns, url
from family.views import MemberDetailView, TreeView,HybridDetailView, ContactView
from family.models import Member
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
    url(r'^tree/$', TreeView.as_view(), name='family-tree'),
    url(r'^member/(?P<pk>\d+)/$', HybridDetailView.as_view(model=Member), name='member-detail'),
    url(r'^contact/$', login_required(ContactView.as_view()), name='family-contact'),
   
)
