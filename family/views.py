from family.models import Member
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
import simplejson as json
import datetime
from dateutil import tz


class MemberDetailView(DetailView):

    model = Member

class TreeView(TemplateView):
    template_name = "family/treeview.html"  

    def encode_datetime(obj):
	if isinstance(obj, datetime.datetime):
		return obj.astimezone(tz.tzutc()).strftime('%Y-%m-%dT%H:%M:%SZ')
	raise TypeError(repr(o) + " is not JSON serializable") 

    def get_context_data(self, **kwargs):
        context = super(TreeView, self).get_context_data(**kwargs)        
        context['tree'] = Member.get_annotated_list()
        return context
