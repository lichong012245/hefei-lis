from django.shortcuts import render, redirect
from family.forms import UserProfileForm
from family.models import Article
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django import forms
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


class ContactForm(forms.Form):
    sender = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'id':'sender'}))
    subject = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'id':'subject'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'id':'email'}))
    message=forms.CharField(widget=forms.Textarea(attrs={'id':'message'}))

def Index(request):
    return render(request,'lis/index.html')

def Gallery(request):
    return render(request,'lis/gallery.html')


def Contact(request):
      if request.method == 'POST':
         form = ContactForm(request.POST)
         if form.is_valid():
              subject = form.cleaned_data['subject']
              sender = form.cleaned_data['sender']
              message = form.cleaned_data['message']
              email = form.cleaned_data['email']
              send_mail(subject,message,sender+'<'+email+'>',['lishefei@gmail.com'],fail_silently=False)
              return redirect('index')  
      else:
              form = ContactForm()
      return render(request, 'lis/contact.html',{'form':form})


def UserProfile(request):      
      if request.method == 'POST':           
           profile_form = UserProfileForm(data=request.POST)
           if profile_form.is_valid():    
               profile = profile_form.save(commit=False)
               profile.user=request.user
               profile.save()
               return redirect('index')
      else:              
             profile_form=  UserProfileForm()                
      return render(request, 'registration/profile.html',{'profile_form':profile_form})

@login_required
def ShowArticle(request):
  object_articles = Article.objects.filter(is_display=True)
  return render(request,'lis/article.html',{'articles':object_articles})
