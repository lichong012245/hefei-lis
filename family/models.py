# -*- coding: utf-8 -*-
from django.db import models
from treebeard.mp_tree import MP_Node
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile
import io, os
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models.signals import post_save


class Member(MP_Node):
   male_or_female=(
('M',u'男'),
('F',u'女'),
)
   tree_branch=(
('1',u'瀚章支系'),
('2',u'鸿章支系'),
('3',u'鹤章支系'),
('4',u'蕴章支系'),
('5',u'凤章支系'),
('6',u'昭庆支系'),
)
   name = models.CharField(max_length=100)   
   date_of_birth = models.DateField(blank=True)
   sex = models.CharField(choices=male_or_female,max_length=10)
   desc=models.TextField(blank=True)
   phone = models.CharField(max_length=100,blank=True,null=True)
   address = models.CharField(max_length=5000,blank=True,null=True)
   email = models.EmailField(blank=True,null=True)
   branch=models.CharField(choices=tree_branch,max_length=10,blank=True)   

   
   def __unicode__(self):
        return self.name

class UserProfile(models.Model):
  tree_branch=(
('1',u'瀚章支系'),
('2',u'鸿章支系'),
('3',u'鹤章支系'),
('4',u'蕴章支系'),
('5',u'凤章支系'),
('6',u'昭庆支系'),
)
  user=models.OneToOneField(User)
  member=models.OneToOneField(Member,blank=True,null=True)
  self_desc=models.TextField(blank=True)
  branch=models.CharField(choices=tree_branch,max_length=10,blank=True)

  def __unicode__(self):
     return self.user.username
  
 
class postimage(models.Model):
    image=models.ImageField(upload_to='family/orig/',blank=True, null=True)
    thumbnail=models.ImageField(upload_to='family/thumbnail/',blank=True, null=True,editable=False)
    member=models.ForeignKey(Member)

    def __str__(self):
        return self.image.name

    def save(self):
        THUMBNAIL_SIZE = (128, 128)
        image=Image.open(self.image)
        if image.mode not in ('L', 'RGB'):
          image = image.convert('RGB')
        image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)
        temp_handle = io.BytesIO()
        image.save(temp_handle, 'png')
        temp_handle.seek(0)
        suf = SimpleUploadedFile(os.path.split(self.image.name)[-1],
                temp_handle.read(), content_type='image/png')
        self.thumbnail.save(suf.name+'.png', suf, save=False)
        super(postimage,self).save()

## send email when user is created
class Article(models.Model):
    title=models.CharField(max_length=225)
    author=models.CharField(max_length=225,blank=True,null=True)
    body=models.TextField()
    is_display=models.BooleanField()

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __unicode__(self):
        return self.title
    


def send_notification(sender,instance,created,**kwargs):
   if created:
            message = u"有新用户注册："+ instance.last_name + instance.first_name +"    "+ r"www.hefei-lis.com/admin/auth/user/"+str(instance.pk)
            subject = instance.username+u"刚刚注册，请查看"
            send_mail(subject,message,'noreply@hefei-lis.com',['lishefei@gmail.com'],fail_silently=False)

post_save.connect(send_notification,sender=User)
            