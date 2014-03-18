from django.conf.urls import patterns, url
from family.views import MemberDetailView, TreeView,HybridDetailView, ContactView
from family.models import Member


urlpatterns = patterns('',
    url(r'^tree/$', TreeView.as_view(), name='family-tree'),
    url(r'^member/(?P<pk>\d+)/$', HybridDetailView.as_view(model=Member), name='member-detail'),
    url(r'^contact/$', ContactView.as_view(), name='family-contact'),
   
)
