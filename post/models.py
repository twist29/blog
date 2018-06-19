from django.db import models
from django.urls import reverse
#from django.utils.text import slugify
from ckeditor.fields import RichTextField
#from __future__ import unicode_literals
#from django.contrib.auth.models import User


class Post(models.Model):
   # user = models.ForeignKey('auth.User', verbose_name='Writer', related_name='posts')
    title = models.CharField(max_length=120, verbose_name="Title")
    content = RichTextField(verbose_name="Content")
    publishing_date = models.DateTimeField(verbose_name="Published Date", auto_now_add=True)#auto_now_add deðiþtiremezsin  sadece o zaman ki yayýmlanmayý tarihini gösterir.
    image= models.ImageField(null=True, blank=True)
    #slug= models.SlugField(unique=True, editable=False, max_length=130)
    
    def __str__(self):
        return self.title
 
    
    def get_absolute_url(self):
       return reverse('post:detail', kwargs={'id': self.id})
       # return "/post/{}".format(self.id)
       
    def get_create_url(self):
       return reverse('post:create')
   
    def get_update_url(self):
       return reverse('post:update', kwargs={'id': self.id})
   
    def get_delete_url(self):
       return reverse('post:delete', kwargs={'id': self.id})
    
  #  def get_unique_slug(self):
        
   #     slug= slugify(self.title.replace('unicode_escape','utf-8'))
    #    unique_slug= slug
     #   counter= 1
      #  while Post.objects.filter(slug=unique_slug).exists():
       #     unique_slug= '{}-{}'.format(slug, counter)
        #    counter += 1
         #   return unique_slug
        
    
   # def save(self, *args, **kwargs):
     #    if not self.id:
      #      self.slug = slugify( self.title )
       #     models.Model.save(self, *args, **kwargs )
   
    class Meta:
        ordering=['-publishing_date', 'id' ]         