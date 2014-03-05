from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from family.models import Member, postimage, UserProfile
from django import forms
from family.forms import UserProfileAdminForm


class ImageInline(admin.TabularInline):
    model = postimage


class MyAdmin(TreeAdmin):
    form = movenodeform_factory(Member)
    inlines = [
        ImageInline,
    ]
    
class UserProfileAdmin(admin.ModelAdmin):
    form = UserProfileAdminForm


admin.site.register(Member, MyAdmin)
admin.site.register(UserProfile,UserProfileAdmin)