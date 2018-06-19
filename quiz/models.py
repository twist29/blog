from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

class Question(models.Model):
    level = models.CharField(max_length=120, verbose_name="Level")
    content = RichTextField(verbose_name="Content")
    publishing_date = models.DateTimeField(verbose_name="Published Date", auto_now_add=True)
    image= models.ImageField(null=True, blank=True)
    
    
    def __str__(self):
        return self.level
 

   
    class Meta:
        verbose_name_plural='Questions'
        ordering=['-publishing_date', 'id' ]         