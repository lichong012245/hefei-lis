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
           r=list(object.postimage_set.all()[:1])
           if r:
                return r[0].thumbnail.url
           return None

@dajaxice_register
def get_member(req, pk):
    dajax = Dajax()
    p = Member.objects.get(pk=pk)
    dajax.assign('#image', 'src', get_first_thumbnail_of_member(p))
    dajax.assign('#name', 'innerHTML', p.name)
    dajax.assign('#sex', 'innerHTML', show_sex_in_chinese(p.sex))    
    dajax.assign('#desc', 'innerHTML', linebreaksbr(p.desc))         
    return dajax.json()
