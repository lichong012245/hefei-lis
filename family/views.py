from family.models import Member
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView

class MemberDetailView(DetailView):

    model = Member

class TreeView(TemplateView):
    template_name = "family/treeview.html"

    def get_context_data(self, **kwargs):
        context = super(TreeView, self).get_context_data(**kwargs)        
        context['tree'] = Member.dump_bulk()
        return context
