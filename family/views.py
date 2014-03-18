from family.models import Member
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
import simplejson
from django.http import HttpResponse
from django.views.generic.detail import BaseDetailView, SingleObjectTemplateResponseMixin
from django.core import serializers


class ContactView(TemplateView):
     template_name = "family/contactview.html"      

class JSONResponseMixin(object):
    def render_to_response(self, context):
        return self.get_json_response(self.convert_context_to_json(context))
    def get_json_response(self, content, **httpresponse_kwargs):
        return HttpResponse(content, content_type='application/json', **httpresponse_kwargs)
    def convert_context_to_json(self, context):
        return serializers.serialize('json', context)

class MemberDetailView(DetailView):

    model = Member

class TreeView(TemplateView):
    template_name = "family/treeview.html"      

    def get_context_data(self, **kwargs):
        context = super(TreeView, self).get_context_data(**kwargs)        
        context['tree'] = Member.get_annotated_list()
        return context

class HybridDetailView(JSONResponseMixin, SingleObjectTemplateResponseMixin, BaseDetailView):
    def render_to_response(self, context):
        if self.request.is_ajax():
            obj = context['object']            
            return JSONResponseMixin.render_to_response(self, obj)
        else:
            return SingleObjectTemplateResponseMixin.render_to_response(self, context)
