from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from family.models import Member, postimage, UserProfile
from django import forms


class ImageInline(admin.TabularInline):
    model = postimage

class UserProfileForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea)
    class Meta:
            model = UserProfile

class MyAdmin(TreeAdmin):
    form = movenodeform_factory(Member)
    inlines = [
        ImageInline,
    ]
    
class UserProfileAdmin(admin.ModelAdmin):
    form = UserProfileForm


admin.site.register(Member, MyAdmin)
admin.site.register(UserProfile,UserProfileAdmin)