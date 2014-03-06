from django.shortcuts import render
from family.forms import UserProfileForm,UserFormForFront
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

def UserProfile(request):
      if request.method == 'POST':
          user_ = User.objects.get(pk=request.user.pk)
           user_form = UserFormForFront(data=request.POST)
           profile_form = UserProfileForm(data=request.POST)
           if profile_form.is_valid() and user_form.is_valid():
               
               user_= user_form.save()
               profile = profile_form.save(commit=False)
               profile.user=user_
               profile.save()
               return HttpResponseRedirect('/family/tree/')
      else:  
               profile_form=  UserProfileForm() 
               user_form = UserFormForFront()
      return render(request, 'registration/profile.html',{'user_form':user_form,'profile_form':profile_form})