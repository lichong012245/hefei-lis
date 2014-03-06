from django import forms
from django.contrib.auth.models import User
from family.models import UserProfile
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
 
    class Meta:
             model = User
             fields = ('username','email')

class UserFormForFront(forms.ModelForm):
   

   class Meta:
         model= User
         fields = ('first_name','last_name','email')


class UserForm(forms.ModelForm):
   password= forms.CharField(widget=forms.PasswordInput())

   class Meta:
         model= User


class UserProfileAdminForm(forms.ModelForm):
    self_desc = forms.CharField(widget=forms.Textarea)
    class Meta:
            model = UserProfile
            

class UserProfileForm(forms.ModelForm):
    self_desc = forms.CharField(widget=forms.Textarea)
    class Meta:
            model = UserProfile
            fields=('self_desc',)