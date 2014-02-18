from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from family.models import Member

class MyAdmin(TreeAdmin):
    form = movenodeform_factory(Member)

admin.site.register(Member, MyAdmin)
