from dajaxice.decorators import dajaxice_register
from dajax.core import Dajax
from family.models import Member

@dajaxice_register
def get_member(req, pk):
    dajax = Dajax()
    p = Member.objects.get(pk=pk)
    dajax.assign('#name', 'innerHTML', p.name)
    dajax.assign('#sex', 'innerHTML', p.sex)    
    dajax.assign('#desc', 'innerHTML', p.desc)    
    dajax.assign('#branch', 'innerHTML', p.branch)    
    return dajax.json()