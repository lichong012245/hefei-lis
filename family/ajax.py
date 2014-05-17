# -*- coding: utf-8 -*-
from dajaxice.decorators import dajaxice_register
from dajax.core import Dajax
from family.models import Member, postimage
from django.template.defaultfilters import linebreaksbr

def show_sex_in_chinese(sex):
      if sex == 'M':
             return u'男'
      else:
             return u'女'

def get_first_thumbnail_of_member(object):
         try:
           r=list(object.postimage_set.order_by('id')[0])
           if r:
                return r[0].thumbnail.url
         except IndexError:       
           return 'https://lishefei.s3.amazonaws.com/lis/images/lhz/placeholder.png'

def get_nth_item_image_of_member(object,n):
  r=list(object.postimage_set.order_by('id')[n-1:n])
  if r:
    return r[0].image.url
  return ''  

@dajaxice_register
def get_member(req, pk):
    dajax = Dajax()
    p = Member.objects.get(pk=pk)
    dajax.assign('#image', 'src', get_first_thumbnail_of_member(p))
    dajax.assign('#name', 'innerHTML', p.name)
    dajax.assign('#sex', 'innerHTML', show_sex_in_chinese(p.sex))    
    dajax.assign('#desc', 'innerHTML', linebreaksbr(p.desc))  
    dajax.assign('#image1', 'src', get_nth_item_image_of_member(p,2))
    dajax.assign('#image2', 'src', get_nth_item_image_of_member(p,3))
    dajax.assign('#image3', 'src', get_nth_item_image_of_member(p,4))
    dajax.assign('#image4', 'src', get_nth_item_image_of_member(p,5))
       
    return dajax.json()
