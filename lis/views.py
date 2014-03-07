from django.shortcuts import render
from family.forms import UserProfileForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.template import RequestContext

def Index(request):
    return render(request,'lis/index.html')

def Contact(request):
      return render(request, 'lis/contact.html')

def UserProfile(request):      
      if request.method == 'POST':           
           profile_form = UserProfileForm(data=request.POST)
           if profile_form.is_valid():    
               profile = profile_form.save(commit=False)
               profile.user=request.user
               profile.save()
               return HttpResponseRedirect('/family/tree/')
      else:  
               profile_form=  UserProfileForm()                
      return render(request, 'registration/profile.html',{'profile_form':profile_form})