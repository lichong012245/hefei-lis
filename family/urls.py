from django.conf.urls import patterns, url
from family.views import MemberDetailView, TreeView,HybridDetailView
from family.models import Member


urlpatterns = patterns('',
    url(r'^tree/$', TreeView.as_view(), name='family-tree'),
    url(r'^member/(?P<pk>\d+)/$', HybridDetailView.as_view(model=Member), name='member-detail'),
   
)
