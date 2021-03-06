
# Create your models here.

from django.db import models
from treebeard.mp_tree import MP_Node
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile
import io

class Member(MP_Node):
   male_or_female=(
('M','Male'),
('F','Female'),
)
   name = models.CharField(max_length=30)
   date_of_birth = models.DateField(blank=True)
   sex = models.CharField(choices=male_or_female,max_length=10)
   desc=models.CharField(max_length=5000)
   image=models.ImageField(upload_to='family/thumbnail/',blank=True, null=True,editable=False)

   node_order_by = ['name']
   def __unicode__(self):
        return 'Name: %s' % self.name
 
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
        super(Member,self).save()
