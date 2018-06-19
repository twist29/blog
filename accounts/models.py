from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

def upload_to(instance,filename):
        return '%s%s%s'%('profile_photo',instance.user.username,filename)

class UserProfile(models.Model):
    MALE='M'
    FEMALE='F'
    OTHER='O'
    SEX=((MALE,'MALE'), (FEMALE,'FEMALE'),(OTHER,'OTHER'))
    
    user=models.OneToOneField(User,on_delete=models.CASCADE,verbose_name='User')
    phone_number= models.CharField(max_length=11,verbose_name='Phone Number',blank=True)
    sex= models.CharField(max_length=1,default=3,verbose_name='Sex',choices=SEX,blank=True)
    description = models.TextField(max_length=500,verbose_name='Description',blank=True)
    birth=models.DateField(blank=True,verbose_name='Birth Date',null=True)
    city = models.CharField(max_length=100, default='')
    profile_photo = models.ImageField(upload_to=upload_to,verbose_name='Profile Photo',default='profile_photo/default_user.jpg', blank=False,null=True)


    class Meta:
        verbose_name_plural='User Informations'
        
    def __str__(self):
        return "%s Profile"%(self.user.get_full_name())
    
def create_user_profile(instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        
post_save.connect(receiver=create_user_profile, sender=User)   
    
    