from django.conf.urls import patterns, url
from family.views import MemberDetailView, TreeView


urlpatterns = patterns('',
    url(r'^tree/$', TreeView.as_view(), name='family-tree'),
    url(r'^member/(?P<pk>\d+)/$', MemberDetailView.as_view(), name='member-detail'),
)
