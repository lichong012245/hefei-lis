from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from family.models import Member, postimage


class ImageInline(admin.TabularInline):
    model = postimage


class MyAdmin(TreeAdmin):
    form = movenodeform_factory(Member)
    inlines = [
        ImageInline,
    ]



admin.site.register(Member, MyAdmin)
